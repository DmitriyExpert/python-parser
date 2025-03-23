import requests
from bs4 import BeautifulSoup
import json

# Функция для возвращения статус кода подключения к сайту

def statusCode(site_url):
    response = requests.get(site_url);
    return response

def parser_to_site(site_url, output_format="json", output_file="tagil_news"):
    # Проверка исключения при запросе к сайту
    response = statusCode(site_url)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
        return
    
    # Сделаем так, чтобы BeautifulSoup прошел по странице и нашел отдельные блоки с новостями
    
    soup = BeautifulSoup(response.content, 'html.parser')
    newsItem = soup.find_all("div", class_="inside")
    news_data = []
    print(newsItem[1])
    # for item in newsItem:


parser_to_site('https://www.tagil-tv.ru/news')



