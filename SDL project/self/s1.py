import requests
from bs4 import BeautifulSoup

with open("home.html", "r") as f:
    html_doc = f.read()
    
urls = [
     "https://www.google.com/search?q=jobs"
     "https://www.govtjobs.co.in/psu-jobs/"
    ]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")   

if response.status_code == 201:
    print('successful')
else:
    print('Error', response.text)
    
    
job_listings = soup.find_all('div', {'class': 'some-class'}) 

for job_listing in job_listings:

    job_title = job_listing.find('h2', {'class': 'some-class'}).text.strip()
    job_description = job_listing.find('p', {'class': 'some-class'}).text.strip()
    job_link = job_listing.find('a', {'class': 'some-class'})['href']

    print(f"Job Title: {job_title}")
    print(f"Job Description: {job_description}")
    print(f"Job Link: {job_link}")
    print("---")

def fectch_api():
    urls = [
    "https://www.google.com/search?q=jobs",
    "https://govtjobguru.in/govt-jobs-by-department/govt-jobs-in-psu/"
]
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data"

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())

# s= soup.find(id = "link3")
# print(s.get("href"))

# url =https://govtjobguru.in/govt-jobs-by-department/govt-jobs-in-psu/
# # Set up your API credentials
# api_key = "https://www.google.com/"

# # Set up the API request
# url = "https://serpapi.com/search"
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {api_key}"
# }
# params = {
#     "q": "software engineer",
#     "location": "New York, NY",
#     "tbm": "jbs"
# }

# # Make the API request
# response = requests.get(url, headers=headers, params=params)

# # Parse the response
# if response.status_code == 200:
#     job_listings = response.json()["organic_results"]
#     for job in job_listings:
#         print(job["title"], job["company"], job["location"])
# else:
#     print("Error:", response.status_code)
    

