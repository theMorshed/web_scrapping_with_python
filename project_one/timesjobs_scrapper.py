from bs4 import BeautifulSoup
import requests
import time

print('Put some skills that are not familiar with')
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_file, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            continue
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        job_link = job.header.h2.a['href']
        
        if unfamiliar_skill in skills:
            continue
        
        with open(f'store/{index}.txt', 'w') as fwrite:
            fwrite.write(f'Company Name: {company_name.strip()}\n')
            fwrite.write(f'Skills: {skills.strip()}\n')
            fwrite.write(f'More Info: {job_link}\n')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes...')
        time.sleep(time_wait * 60)
    