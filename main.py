from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://fiestafarms.ca/employment-opportunities"
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