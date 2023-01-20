import requests
from bs4 import BeautifulSoup
import pandas


URL_TEMPLATE = 'https://sibsutis.ru/students/study/Расписание%20зимней%20сессии/2022-2023%20%20уч.год/ИИВТ'
FILE_NAME = "test.csv"
domain = 'https://sibsutis.ru'


def get_categories(href):
    return href.lstrip('https://sibsutis.ru/students/study/').split('/')


def parser(url=URL_TEMPLATE):
    result_list = {'name': [], 'url_downoload': [], 'categories': []}
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    element_title = soup.find_all('a', class_='element-title')
    if len(element_title) != 0:
        for tag in element_title:
            result_list['name'].append(tag.text)
            result_list['url_downoload'].append(domain + str(tag['data-bx-src']))
            result_list['categories'].append(get_categories(url))
    section_title = soup.find_all('a', class_='section-title')
    if len(section_title) != 0:
        for tag in section_title:
            res = parser(domain + str(tag['href']))
            result_list['name'].extend(res['name'])
            result_list['url_downoload'].extend(res['url_downoload'])
            result_list['categories'].extend(res['categories'])
    return result_list


def main():
    df = pandas.DataFrame(data=parser())
    df.to_csv(FILE_NAME)
    print(df)


if __name__ == '__main__':
    main()
