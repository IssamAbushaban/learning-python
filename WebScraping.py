import os
import requests

# Clear Console
os.system('clear')

reqURL = "https://www.geeksforgeeks.org/python-programming-language/"

# lets make a GET request
print("Requesting Scrape Of " + reqURL + "\n")
reqGET = requests.get(reqURL)

# Did it succeed?
print("Status Returned: " + str(reqGET.status_code) + "\n")
if (reqGET.status_code == 200):
    # print content of request
    print(str(reqGET.content) + "\n")