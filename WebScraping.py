import os
# This is to help us make HTTP request
import requests
# This is to make the text coming from the site more readible
from bs4 import BeautifulSoup
# So we can save our information
import csv

# Clear Console
os.system('clear')

# The Site I will scrape from
reqURI = "https://www.geeksforgeeks.org/python-programming-language/"

# lets make a GET request
print("Requesting Scrape Of " + reqURI + "\n")
reqGET = requests.get(reqURI)

# Did it succeed?
print("Status Returned: " + str(reqGET.status_code) + "\n")
if (reqGET.status_code != 200):
    print("Looks like we are done here :(\n")
    raise SystemExit
    
# Use Beautiful Soup to clean that html!
soupOfURI = BeautifulSoup(reqGET.content, 'html.parser')

# Print content of request
# print(soupOfURI.prettify() + "\n")

# Getting the title tag
print(soupOfURI.title)
 
# Getting the name of the tag
print(soupOfURI.title.name)
 
# Getting the name of parent tag
print(soupOfURI.title.parent.name)

# Finding Content By ID (main div)
htmlContentFoundByID = soupOfURI.find('div', id= 'main')

# Finding Content By Class (leftbarList list)
htmlContentFoundByClassFromSmallerSample = htmlContentFoundByID.find('ul', class_='leftBarList')

# All the li under the above ul
allLiUnderLeftBarList = htmlContentFoundByClassFromSmallerSample.find_all('li')

titleList = list()
count = 1

for line in allLiUnderLeftBarList:
    print(line.text)
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = line.text
    count += 1
    titleList.append(d)

fileToWriteOut = 'titles.csv'
with open(fileToWriteOut, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
    w.writerows(titleList)