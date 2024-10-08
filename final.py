from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def indgovtjobs():
    url = "https://www.indgovtjobs.in/2019/07/PSU-Govt-Jobs.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = []
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            if columns:
                
                post_name = columns[0].text.strip()
                total_vacancies = columns[1].text.strip() if len(columns) > 1 else ''
                closing_date = columns[2].text.strip() if len(columns) > 2 else ''
                details = columns[3].text.strip() if len(columns) > 3 else ''
                apply_link = ''
                if len(columns) > 4:
                    apply_link_tag = columns[4].find('a')
                    if apply_link_tag:
                        apply_link = apply_link_tag['href']

                job = {
                    'Post Name': post_name,
                    'Total Vacancies': total_vacancies,
                    'Closing Date': closing_date,
                    'Details': details,
                    'Apply Link': apply_link
                }
                jobs.append(job)
    return jobs

def govtjobguru():
    url = "https://govtjobguru.in/jobs/ongc-apprentice-recruitment-2024/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = []
    job_list = soup.find_all('div', class_='post-content') 
    for job_entry in job_list:
        title = job_entry.find('h3').text.strip() if job_entry.find('h3') else 'N/A'
        details = job_entry.find('p').text.strip() if job_entry.find('p') else 'N/A'
        apply_link = job_entry.find('a')['href'] if job_entry.find('a') else 'N/A'
        closing_date = 'N/A'

        job = {
            'Post Name': title,
            'Total Vacancies': 'N/A', 
            'Closing Date': closing_date,
            'Details': details,
            'Apply Link': apply_link
        }
        jobs.append(job)
    return jobs

@app.route('/')
def index():
    jobs_indgovt = indgovtjobs()
    jobs_govtjobguru = govtjobguru()
    all_jobs = jobs_indgovt + jobs_govtjobguru 
    return render_template('index.html', jobs=all_jobs)

if __name__ == '__main__':
    app.run(debug=True)

