#Work in progress
#Sub Domain finder using crt

import requests, json, re
from bs4 import BeautifulSoup
print("Subdomain Finder")

#https://crt.sh/?q=%.google.com&output=json
domain = "starbucks.com"
crtUrl = "https://crt.sh/?q=%." + domain + "" #
print("Fetching:", crtUrl)

domains = requests.get(crtUrl)
test = BeautifulSoup(domains.text, "html.parser")
#test.decode('utf-8')


match = re.findall(r'<TD>(.*?)\.' + domain + '</TD>', domains.text) #works
#print(match)
for dom in match:
    if "<BR>" in dom:
        dom.replace("<BR>","\n")
        #print("br one")
    print(match)

