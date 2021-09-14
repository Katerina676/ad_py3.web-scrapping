import requests
from bs4 import BeautifulSoup as bs

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/all/'


def scrape_article(key, url):
    resp = requests.get(url)
    soup = bs(resp.text, 'html.parser')
    articles = soup.find_all('article')
    new_list = []
    for article in articles:
        headlines = article.h2.a.text
        date_post = article.find('span', class_='tm-article-snippet__datetime-published').text
        post_link = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
        post_text = article.find('div', class_='tm-article-body tm-article-snippet__lead').text
        for words in key:
            if (words.lower() in headlines.lower()) or (words.lower() in post_text.lower()):
                print(f'Дата: {date_post} - Заголовок: {headlines} - Ссылка: {post_link}')
                new_list.append([date_post, headlines, post_link])
    return new_list


if __name__ == '__main__':
    scrape_article(KEYWORDS, URL)