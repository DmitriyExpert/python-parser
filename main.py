import requests
from bs4 import BeautifulSoup
import json

# Функция для возвращения статус кода подключения к сайту

def statusCode(site_url):
    response = requests.get(site_url);
    return response

# Функция сохранения в json 
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Данные сохранены в {filename}")

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
    for item in newsItem:
        try:
            # Заголовки
            titleNews = item.find('div', class_='views-field-title')
            # Запишем в title элемент где хранится заголовок (если он есть), а если нет то title = None
            title = titleNews.text.strip() if titleNews else None

            # Подзаголовки
            subtitleNews = item.find('div', class_='views-field-field-news-body')
            subtitle = subtitleNews.text.strip() if subtitleNews else None

            # Даты
            dateNews = item.find('div', class_='views-field-created-1')
            date = dateNews.text.strip() if dateNews else None

            # Ссылки
            divwithlinkNews = item.find('div', class_='views-field-nothing')
            linkNews = divwithlinkNews.find('a') if divwithlinkNews else None
            link = "https://www.tagil-tv.ru" + linkNews['href'] if linkNews else None

            if (title and subtitle and date and link) == None:
                pass
            else:
                news_data.append({
                    'title': title,
                    'subtitle': subtitle,
                    'date': date,
                    'link': link,
                })
        except Exception as e:
            print(f"Ошибка при обработке новости: {e}")
    
    if output_format == "json":
        save_to_json(news_data, f"{output_file}.json")



parser_to_site('https://www.tagil-tv.ru/news')



