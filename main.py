from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = "https://fiestafarms.ca/employment-opportunities"
def search(url:str):
    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    instances = soup.find_all("em")
    j = 0
    for i in instances:
        if "Part-time" in i:
            print("success")
            print(instances[j-1])
        j += 1
search(url)
url = "https://bestbuycanada.wd3.myworkdayjobs.com/BestBuyCA_Career?geotagText=CA/M6G%204B7/Toronto&distance=677b3630ee5f01a8d7424fdbdb0724d4&timeType=540b7b97140b01bb879ee98c7d1a8400"
def search2(url):
    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    instances = soup.find_all("str")
    print(instances)
    j = 0
    for i in instances:
        if "Part-time" in i:
            print("success")
            print(instances[j - 1])
        j += 1
search2(url)
headers = { 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json,application/xml'}
# I don't know what this code does-
r = requests.get('https://bestbuycanada.wd3.myworkdayjobs.com/BestBuyCA_Career?geotagText=CA/M6G%204B7/Toronto&distance=677b3630ee5f01a8d7424fdbdb0724d4&timeType=540b7b97140b01bb879ee98c7d1a8400', headers=headers)
links = ['https://wd1.myworkdaysite.com' + i['title']['commandLink'] for i in r.json()["body"]['children'][0]['children'][0]['listItems']]
print(links)
