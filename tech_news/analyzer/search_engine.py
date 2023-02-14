from tech_news.database import find_news, search_news
from tech_news.analyzer.utils.convert_news_dict_to_tuple\
    import convert_news_dict_to_tuple
from datetime import datetime
from tech_news.analyzer.utils.filter_news import filter_news


# Requisito 7
def search_by_title(title):
    news_results = filter_news(find_news(), 'title', title)
    return news_results


# Requisito 8
def search_by_date(date: str):
    if date[4] != '-':
        raise ValueError('Data inválida')
    try:
        formated_date = datetime.strptime(date.replace('-', "/"), "%Y/%m/%d")\
            .strftime("%d/%m/%Y")
        news_results = search_news({"timestamp": formated_date})
    except ValueError:
        raise ValueError('Data inválida')
    print(news_results)
    if not news_results or not len(news_results):
        return []
    return convert_news_dict_to_tuple(news_results)


# Requisito 9
def search_by_category(category):
    news_results = filter_news(find_news(), 'category', category)
    return news_results
