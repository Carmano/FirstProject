import requests
from bs4 import BeautifulSoup


URL_TEMPLATE = 'https://sibsutis.ru/students/study/Расписание%20очной%20формы%20обучения/2022-2023%20уч.год/I%20полугодие%202022-2023%20уч.год_/ИИВТ/3%20курс'
DOMAIN = 'https://sibsutis.ru'


def parser(url=URL_TEMPLATE):
    result_list = {'name': [], 'url_downoloads': []}
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    element_title = soup.find_all('a', class_='element-title')
    if len(element_title) != 0:  # Проверяет если в каталоге файлы и записывает их в результат
        for tag in element_title:
            result_list['name'].append(tag.text)
            result_list['url_downoloads'].append(DOMAIN + str(tag['data-bx-src']))
            # result_list['categories'].append(get_categories(url))
    section_title = soup.find_all('a', class_='section-title')
    if len(section_title) != 0:  # Проверяет если в каталоге папки, если есть то заходит внутрь каждой папки.
        for tag in section_title:
            res = parser(DOMAIN + str(tag['href']))
            result_list['name'].extend(res['name'])
            result_list['url_downoloads'].extend(res['url_downoloads'])
            # result_list['categories'].extend(res['categories'])
    return result_list


def get_categories(href):
    return href.lstrip('https://sibsutis.ru/students/study/').split('/')


def download(df):
    for filename, url in zip(df['name'], df['url_downoloads']):
        r = requests.get(url)
        open(f'files/{filename}', 'wb').write(r.content)

