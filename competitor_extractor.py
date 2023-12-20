from src.gmaps import Gmaps
import pandas as pd
import os 
import re
import requests 

input_file = "/home/titan/Desktop/Python/ForMarketing/google-maps-scraper/input/gmaps_lawyers_extract.csv"
links = []
 # Regular expression pattern for Google Maps URLs
pattern = r'https://www\.google\.com/maps/[^\s]+'

sheet_links = ["https://www.google.com/maps/place/Imtilak+Real+Estate/data=!4m7!3m6!1s0x14caba3cb97a6d01:0xa4a65c1b72fca323!8m2!3d41.0640552!4d28.8064807!16s%2Fg%2F11bbww_mlv!19sChIJAW16uTy6yhQRI6P8chtcpqQ?authuser=0&hl=tr&rclk=1","https://www.google.com/maps/place/AX%C4%B0S+LAW+CONSULT%C4%B0NG+%D9%84%D9%84%D9%85%D8%AD%D8%A7%D9%85%D8%A7%D8%A9+%D9%88%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D8%B4%D8%A7%D8%B1%D8%A7%D8%AA+%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%D9%8A%D8%A9+%D9%88%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA+%D8%A7%D9%84%D8%AC%D9%86%D8%B3%D9%8A%D8%A9+%D8%A7%D9%84%D8%AA%D8%B1%D9%83%D9%8A%D8%A9%E2%80%AD/data=!4m7!3m6!1s0x14caa32d30c54835:0x8d9415aa680d3dae!8m2!3d40.9991992!4d28.7990228!16s%2Fg%2F11tjy5ybch!19sChIJNUjFMC2jyhQRrj0NaKoVlI0?authuser=0&hl=tr&rclk=1"]

if(os.path.exists(input_file)):
        df = pd.read_csv(input_file)
        competitors = df['competitors']
        # Iterate through each competitor entry
    
def get_links(competitors):
        for comp in competitors:
            # Assuming each competitor entry contains links separated by some delimiter (e.g., comma)
            if isinstance(comp, str):
                # Assuming each competitor entry contains links separated by some delimiter (e.g., comma)
                comp_links = re.findall(pattern, comp)
                links.extend(comp_links)
        return links

links = get_links(competitors)    
gmap_sample_list= []
sample_count = 0
for link in links:
    #print ("LINK ",link)
    sample_count += 1
    print("LINK ",link)
    gmap_sample_list.append(link)
    if sample_count >= 10:
        break
print("SEARCH RESULT ",gmap_sample_list)    
#sample_links = ["https://www.google.com/maps/place/?q=place_id:ChIJ4V1pIhSjyhQR_Iwc9s4fhnM"]
#Gmaps.links(links=sample_links,output_folder="/test")  

# Example usage

