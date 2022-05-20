from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait   #웹을 기다려주는 기능
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://quotes.toscrape.com/login"

chrome_options = webdriver.ChromeOptions()
my_crawling_browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
my_crawling_browser.get(url=URL)

#ID가 username가 보일때까지 기다려라
WebDriverWait(my_crawling_browser, 10).until(ec.presence_of_element_located(By.ID,"username"))