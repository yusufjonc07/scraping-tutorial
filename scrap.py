import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Function to scrape a single page
def scrape_page(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find and process the desired data on the page
        # For example, let's find all the <h2> tags and print their text
        headings = soup.find_all('h2')
        for heading in headings:
            print("Heading:", heading.text.strip())
    else:
        print(f"Failed to retrieve the webpage: {url}")

# Function to scrape multiple pages with pagination
def scrape_multiple_pages(base_url, num_pages):
    # Initialize a Selenium WebDriver
    driver = webdriver.Chrome()
    # Set a wait time for the driver to wait for elements to appear
    wait = WebDriverWait(driver, 10)
    
    try:
        # Loop through each page
        for page in range(1, num_pages + 1):
            # Construct the URL for the current page
            url = f"{base_url}?query=принтер&needsCorrection=1&currentPage={page}"
            # Open the URL in the WebDriver
            driver.get(url)
            
            # Wait for the dynamically loaded content to appear
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'some-class')))
            
            # Get the page source after content is loaded
            page_source = driver.page_source
            
            # Parse the HTML content of the page
            soup = BeautifulSoup(page_source, 'html.parser')
            # Find and process the desired data on the page
            # For example, let's find all the <h2> tags and print their text
            headings = soup.find_all('h2')
            for heading in headings:
                print("Heading:", heading.text.strip())
            
            # Optional: You can also scrape additional data from the page using BeautifulSoup
            
            # Simulate a human-like behavior by waiting for a random amount of time
            time.sleep(2)
    
    finally:
        # Close the WebDriver
        driver.quit()

# Example usage
base_url = 'https://uzum.uz/ru/search'
num_pages = 3
scrape_multiple_pages(base_url, num_pages)
