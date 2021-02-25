from bs4 import BeautifulSoup
import requests
import lxml


#Пошук вакансій чітко по Python вся країна
url = 'https://www.work.ua/jobs-python-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%96%D1%81%D1%82/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'lxml')
jobs = soup.find_all('div', class_="card card-hover card-visited wordwrap job-link")


# пошук даних вакансії 1 сторінка
for job in jobs:
	company_name = job.find('div', class_='add-top-xs').text
	Language = job.find('h2').text
	text = job.find('p', class_='overflow text-muted add-top-sm add-bottom').text
	date_ = job.find('span', class_= 'text-muted small').text

	#пошук ссилок
	for el in job.select('h2'):
		url_more = el.select_one('a').get('href')

#Вивід даних в консоль
	print('-----------------------------------------------------')
	
	print(f'''
    COMPANY BAME: {company_name}
    LANGUAGE: {Language}
    INFORMATION: {text}
    DATE: {date_}
    URL: https://www.work.ua{url_more}''')

if __name__ == "__main__":
    main()
