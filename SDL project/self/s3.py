from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup 
import flask
with open("home.html", "r") as f:
    html_doc = f.read()

driver = webdriver.Chrome()
query = "Laptop"


time.sleep(10)
driver.close()

