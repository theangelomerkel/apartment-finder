# apartment-finder
a tool to find an apartment faster on websites
import requests
from bs4 import BeautifulSoup

# specify the url
url = "https://www.immobilienscout24.de/?seaid=g_brand&gclid=EAIaIQobChMIsKausNfQ_AIVE4bVCh2D-APxEAAYASAAEgJdSPD_BwE"

# send a request to the website
response = requests.get(url)

# parse the html content
soup = BeautifulSoup(response.content, "html.parser")

# find all the apartments on the page
apartments = soup.find_all("div", class_="placard")

# print the details of each apartment
for apartment in apartments:
    name = apartment.find("span", class_="altRentDisplay").text
    price = apartment.find("span", class_="altRentDisplay").text
    location = apartment.find("div", class_="location").text
    print("Name:", name)
    print("Price:", price)
    print("Location:", location)
    
SyntaxError: multiple statements found while compiling a single statement
import requests
from bs4 import BeautifulSoup

# specify the url
url = "https://www.immobilienscout24.de/?seaid=g_brand&gclid=EAIaIQobChMIsKausNfQ_AIVE4bVCh2D-APxEAAYASAAEgJdSPD_BwE"

# send a request to the website
response = requests.get(url)

# parse the html content
soup = BeautifulSoup(response.content, "html.parser")

# find all the apartments on the page
apartments = soup.find_all("div", class_="placard")

# print the details of each apartment
for apartment in apartments:
    name = apartment.find("span", class_="altRentDisplay").text
    price = apartment.find("span", class_="altRentDisplay").text
    location = apartment.find("div", class_="location").text
    print("Name:", name)
    print("Price:", price)
    print("Location:", location)
    
