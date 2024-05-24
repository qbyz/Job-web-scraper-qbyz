from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://fiestafarms.ca/employment-opportunities"
def fiesta(url:str):
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
fiesta(url)

url = "https://bestbuycanada.wd3.myworkdayjobs.com/BestBuyCA_Career?geotagText=CA/M6G%204B7/Toronto&distance=677b3630ee5f01cec31b4fdbdb0723d4&timeType=540b7b97140b01bb879ee98c7d1a8400"
selector = ".css-19uc56f"
def bestBuy(url:str, selector:str, desc_selector:str):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    driver.get(url)

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    job_listings = driver.find_elements(By.CSS_SELECTOR, selector)
    if url != "https://bestbuycanada.wd3.myworkdayjobs.com/BestBuyCA_Career?geotagText=CA/M6G%204B7/Toronto&distance=677b3630ee5f01cec31b4fdbdb0723d4&timeType=540b7b97140b01bb879ee98c7d1a8400":
        job_descs = driver.find_elements(By.CSS_SELECTOR, desc_selector)
        for job, desc in zip(job_listings, job_descs):
            print("Job Title:", job.text)
            print("Job Description:", desc.text)
    else:
        for job in job_listings:
            print(job.text)

    driver.quit()
bestBuy(url, selector, " ")
url = "https://careers.smartrecruiters.com/IndigoBooksMusic/retail?search=toronto"
selector = ".details-title.job-title.link--block-target"
descselector = ".details-desc.job-desc"
bestBuy(url,selector,descselector)
