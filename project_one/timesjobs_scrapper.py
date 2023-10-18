from bs4 import BeautifulSoup
import requests

html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_file, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        continue
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')
    job_link = job.find('div', class_='applied-dtl clearfix').a['href']
    
    print(f'Company Name: {company_name.strip()}')
    print(f'Skills: {skills.strip()}')
    print(f'More Info: {job_link}')
    