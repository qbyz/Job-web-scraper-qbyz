from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def bestBuy(url:str):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".gwt-Anchor")))

    job_listings = driver.find_elements(By.CSS_SELECTOR, ".gwt-anchor")

    for job in job_listings:
        print(job.text)

    driver.quit()
bestBuy(url)
for job in job_listings:
    print(job.text)

driver.quit()
