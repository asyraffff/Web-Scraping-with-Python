from bs4 import BeautifulSoup
import requests

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=') # will return code status only
# print(html_text) 

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml') # lxml : parser
# print(soup.prettify())
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# print(jobs)
company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
skills = job.find('span', class_='srp-skills').text.replace(' ', '')
published_date = job.find('span', class_='sim-posted').text
# print(published_date)
print(f'''
Company name : {company_name}
Required skills : {skills}
Published date : {published_date}
''')
# for job in jobs:
    