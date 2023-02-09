from tech_news.database import search_news
from tech_news.analyzer.utils.convert_news_dict_to_tuple\
    import convert_news_dict_to_tuple


# Requisito 7
def search_by_title(title):
    news_results = search_news({"title": {"$regex": f".*{title}.*",
                                "$options": "i"}})
    return convert_news_dict_to_tuple(news_results)


# Requisito 8
def search_by_date(date):
    news_results = search_news({"timestamp": date})
    return news_results


# Requisito 9
def search_by_category(category):
    news_results = search_news({"category": {"$regex": f".*{category}.*",
                                "$options": "i"}})
    return convert_news_dict_to_tuple(news_results)
