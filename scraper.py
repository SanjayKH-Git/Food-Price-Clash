import time
import csv
import concurrent.futures
import requests
from bs4 import BeautifulSoup as Bs
from lxml import etree
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get("https://chat.openai.com/")
print(driver.pagesource())
