from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def convert_search_to_place_url(search_url):
    # Set up Chrome options for headless mode
    options = Options()
    options.headless = True

    # Initialize the WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Navigate to the search URL
    driver.get(search_url)

    # Wait for potential redirects to complete
    driver.implicitly_wait(10)

    # Get the current URL after redirection
    place_url = driver.current_url

    # Close the browser
    driver.quit()

    return "place_url : "+place_url

# Example Usage
search_url = "https://www.google.com/maps/search/AVUKAT+SAL%C4%B0H+DO%C4%9EAN/@40.992289799999995,28.8439327?authuser=0&hl=tr&entry=ttu"
place_url = convert_search_to_place_url(search_url)
print(place_url)
