from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    news_list = list()
    news_results = search_news({"title": {"$regex": f".*{title}.*",
                                "$options": "i"}})
    for news in news_results:
        curr_news = (news["title"], news["url"])
        news_list.append(curr_news)
    return news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
