import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to chromedriver executable
service = Service('C:/Users/Gourmet/Downloads/chromedriver-win64/chromedriver.exe')

# Specify the path to the Brave executable
chrome_options = Options()
chrome_options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# Initialize the Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a webpage
driver.get('https://www.foxnews.com/')

# Extracting data using BeautifulSoup
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

# Finding and storing headlines using the new class name
for element in soup.findAll(attrs={'class': 'related-body'}):
    name = element.find('a')
    if name:
        results.append(name.text)
    else:
        results.append(element.text)

# Creating a DataFrame
df = pd.DataFrame({'Titles': results})

# Specify full path for CSV file
csv_file_path = 'C:/Users/Gourmet/Desktop/titles.csv'

df.to_csv(csv_file_path, index=False, encoding='utf-8')

# Closing the browser
driver.quit()
