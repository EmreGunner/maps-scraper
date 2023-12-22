import pandas as pd
import requests
import re
import concurrent.futures
import logging
from src.gmaps import Gmaps

# Configure logging
logging.basicConfig(filename='api_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Define your Google Maps API key
API_KEY = 'AIzaSyBKFYUc0NQnSTGjnXCAvyYVAqvRjfqkHhM'

# Caching mechanism to store place_id results
cache = {}
# Initialize counters
processed = 0
found = 0
not_found = 0
found_list = []
link_results = []  # Store results for each link

def prepare_query_from_url(url):
    """
    Prepare a query from a given URL for the Google Maps API.

    This function attempts to extract meaningful parts of the URL,
    such as the name or address, to use as a query.
    """
    try:
        # Extract the main part of the URL
        match = re.search(r'google\.com/maps/search/(.+?)/@', url)
        if match:
            query = match.group(1)
            # Replace URL encoding with actual characters
            query = requests.utils.unquote(query)
            return query
        return None
    except Exception as e:
        logging.error(f"Error in preparing query from URL: {e}")
        return None
    
def get_place_id(link, API_KEY):
    """
    Get place ID from Google Maps API for a given link.
    """
    query = prepare_query_from_url(link)
    if not query:
        logging.info(f"Could not prepare query for link: {link}")
        return None

    if query in cache:
        return cache[query]

    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={query}&inputtype=textquery&fields=place_id&key={API_KEY}"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logging.error(f"API Request Failed: Status Code {response.status_code}, URL: {url}")
            return None

        result = response.json()

        if not result.get('candidates'):
            logging.info(f"No candidates found for query: {query}, Response: {result}")
            return None

        place_id = result['candidates'][0]['place_id']
        cache[query] = place_id
        return place_id
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error for query: {query}, Error: {e}")
        return None
    except Exception as e:
        logging.error(f"General Error for query: {query}, Error: {e}")
        return None

def construct_detailed_url(place_id):
    """
    Construct the detailed Google Maps URL from a place_id.
    """
    return f"https://www.google.com/maps/place/?q=place_id:{place_id}"

def process_link(link, API_KEY):
    """
    Process a single competitor link to get the detailed Google Maps URL.
    """
    place_id = get_place_id(link, API_KEY)
    if place_id:
        return construct_detailed_url(place_id)
    return None

def extract_links(competitors_text):
    """
    Extract links from a string containing competitors information.
    """
    if pd.isna(competitors_text):
        return []
    return re.findall(r'https://www\.google\.com/maps/search/[^\s]+', competitors_text)

def display_progress(total_links, processed, found, not_found):
    """
    Display the progress of processing the competitor links.

    :param total_links: Total number of competitor links.
    :param processed: Number of links processed so far.
    :param found: Number of place IDs found.
    :param not_found: Number of place IDs not found.
    """
    print(f"Total Links: {total_links}, Processed: {processed}/{total_links}, Found: {found}, Not Found: {not_found}")

# Read the input file
input_file = "/home/titan/Desktop/Python/ForMarketing/google-maps-scraper/input/test2 - Get_Competitiros.csv"
df = pd.read_csv(input_file)

# Apply the function to extract links from the 'competitors' column
df['extracted_links'] = df['competitors'].apply(extract_links)

# Flatten the list of lists into a single list of links
all_links = [link for sublist in df['extracted_links'] for link in sublist]

# Remove duplicates from the list
all_links = list(set(all_links))
total_links = len(all_links)
# Process the links in batches with parallel processing
batch_size = 10  # Adjust as needed
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(0, len(all_links), batch_size):
        batch = all_links[i:i + batch_size]
        futures = {executor.submit(process_link, link, API_KEY): link for link in batch}

        for future in concurrent.futures.as_completed(futures):
            original_link = futures[future]  # Get the original link
            detailed_url = future.result()
            processed += 1  # Increment processed counter
            
            # Store the result
            result = {
                'Original Link': original_link,
                'Place ID Found': bool(detailed_url),
                'Detailed URL': detailed_url if detailed_url else 'Not Found'
            }
            link_results.append(result)

            # Update counters
            if detailed_url:
                found += 1
                found_list.append(detailed_url)
            else:
                not_found += 1

            # Display progress
            display_progress(total_links, processed, found, not_found)

# Convert results to a DataFrame
results_df = pd.DataFrame(link_results)

# Export the DataFrame to a CSV file
results_df.to_csv("competitor_placeIds_links.csv", index=False)
#print("FOUND LIST ",found_list)
Gmaps.links(links=found_list,output_folder="/test")  