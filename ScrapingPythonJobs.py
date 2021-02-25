from bs4 import BeautifulSoup
import requests
import lxml
import time



def find_python_vacancy():
	url = 'https://www.work.ua/jobs-python-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%96%D1%81%D1%82/'
	req = requests.get(url).text
	soup = BeautifulSoup(req, 'lxml')
	jobs = soup.find_all('div', class_="card card-hover card-visited wordwrap job-link")

	for index, job in enumerate(jobs):
		company_name = job.find('div', class_='add-top-xs').text
		Language = job.find('h2').text
		text = job.find('p', class_='overflow text-muted add-top-sm add-bottom').text
		date_ = job.find('span', class_= 'text-muted small').text
		for el in job.select('h2'):
			url_more = el.select_one('a').get('href')

		with open(f'src/{index}text', 'w') as f:
			f.write(f'COMPANY NAME: {company_name.strip()}\n')
			f.write(f'LANGUAGE: {Language.strip()}\n')
			f.write(f'INFORMATION: {text.strip()}\n')
			f.write(f'DATE: {date_.strip()}\n')
			f.write(f'URL: https://www.work.ua{url_more}\n')
		print('File Saved')


find_python_vacancy()

if __name__ == '__main__':
	while True:
		find_python_vacancy()
		time_wait = 10
		print(f'Waitting {time_wait} minutes...')
		time.sleep(time_wait * 60)
	
