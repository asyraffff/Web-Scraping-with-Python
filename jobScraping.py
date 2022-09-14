from bs4 import BeautifulSoup
import requests

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=') # will return code status only
# print(html_text) 

## Filter Filter by unfamiliar skills

print('Put some skills that you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')
print('')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml') # lxml : parser
# print(soup.prettify())

######

# For a single job

# job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# # print(jobs)
# company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
# skills = job.find('span', class_='srp-skills').text.replace(' ', '')
# published_date = job.find('span', class_='sim-posted').text
# # print(published_date)
# print(f'''
# Company name : {company_name}
# Required skills : {skills}
# Published date : {published_date}
# ''')

# For all jobs

# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# for job in jobs:
#    published_date = job.find('span', class_='sim-posted').text
#    if 'few' in published_date:
#     company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
#     skills = job.find('span', class_='srp-skills').text.replace(' ', '')
#     more_info = job.header.h2.a['href']
#     print(f"Company name: {company_name.strip()}")
#     print(f"Required skills: {skills.strip()}")
#     print(f"More info: {more_info}")
#     print('')

#     # print(published_date)
#     # print(f'''
#     # Company name : {company_name}
#     # Required skills : {skills}
#     # Published date : {published_date}
#     # ''') 
#     # print('')

# Filter by unfamiliar skills
    
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
   published_date = job.find('span', class_='sim-posted').text
   if 'few' in published_date:
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.lower().replace(' ', '')
    more_info = job.header.h2.a['href']
    if unfamiliar_skills not in skills:
        print(f"Company name: {company_name.strip()}")
        print(f"Required skills: {skills.strip()}")
        print(f"More info: {more_info}")
        print('')

    # print(published_date)
    # print(f'''
    # Company name : {company_name}
    # Required skills : {skills}
    # Published date : {published_date}
    # ''') 
    # print('')