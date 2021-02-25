from bs4 import BeautifulSoup
import requests
import lxml



def find_python_vacancy():
	url = 'https://www.work.ua/jobs-python-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%96%D1%81%D1%82/'
	req = requests.get(url).text
	soup = BeautifulSoup(req, 'lxml')
	jobs = soup.find_all('div', class_="card card-hover card-visited wordwrap job-link")

	for job in jobs:
		company_name = job.find('div', class_='add-top-xs').text
		Language = job.find('h2').text
		text = job.find('p', class_='overflow text-muted add-top-sm add-bottom').text
		date_ = job.find('span', class_= 'text-muted small').text
		for el in job.select('h2'):
			url_more = el.select_one('a').get('href')
		print('-----------------------------------------------------')
		print(f'''
COMPANY NAME: {company_name.strip()}
LANGUAGE: {Language.strip()}
INFORMATION: {text.strip()}
DATE: {date_.strip()}
URL: https://www.work.ua{url_more}''')


find_python_vacancy()
