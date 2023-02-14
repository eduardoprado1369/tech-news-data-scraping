import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            html_content = response.text
            return html_content
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    updates = selector.css('h2.entry-title a ::attr(href)').getall()
    return updates


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css("a.next ::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css('link[rel=canonical] ::attr(href)').get()
    title = selector.css('h1.entry-title ::text').get().strip()
    timestap = selector.css('li.meta-date ::text').get()
    writer = selector.css('li.meta-author span.author ::text').get()
    reading_time_str: str = selector.css('li.meta-reading-time ::text').get()
    # a regex e função a baixo foram retiradas de:
    # https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
    reading_time = int(re.findall(r'\d+', reading_time_str)[0])
    summary = "".join(selector.css('div.entry-content > p:nth-of-type(1)\
         ::text').getall()).strip()
    category = selector.css('span.label ::text').get()
    news_info = {
        "url": url,
        "title": title,
        "timestamp": timestap,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }
    return news_info


# Requisito 5
def get_tech_news(amount: int):
    curr_page = 'https://blog.betrybe.com/'
    all_pages = []
    all_pages.append(curr_page)
    for _ in range(int(amount / 12)):
        curr_page = scrape_next_page_link(fetch(curr_page))
        all_pages.append(curr_page)
    print(all_pages)
    all_links = []
    all_news = []
    while len(all_links) < amount:
        scrape_updates()
    create_news(all_news)
    print(all_news)
    return all_news
