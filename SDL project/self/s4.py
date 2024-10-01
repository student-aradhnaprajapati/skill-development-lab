from flask import Flask, render_template
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    
# @app.route('/jobs')
# def jobs():
#     return render_template('home.html')

# driver = webdriver.Chrome()

# web = requests.get("https://www.google.com/")
# print(web.content)

# soup = BeautifulSoup(web.content, "html.parser")

# time.sleep(4)
# driver.close()
