import requests
from bs4 import BeautifulSoup
import json

# Функция для возвращения статус кода подключения к сайту

def statusCode(site_url):
    response = requests.get(site_url);
    return response

def parser_to_site(site_url, output_format="json", output_file="tagil_news"):
    # Проверка исключения при запросе к сайту
    try:
        statusCode(site_url).raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
        return
    
    # Сделаем так, чтобы BeautifulSoup прошел по странице и нашел отдельные блоки с новостями
    
    


