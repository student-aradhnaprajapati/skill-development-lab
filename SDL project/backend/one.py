import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.codewithharry.com/")
print(web.content)

soup = BeautifulSoup(web.content, "html.parser")