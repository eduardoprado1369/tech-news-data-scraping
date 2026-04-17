from tech_news.database import find_news
from tech_news.analyzer.utils.calculate_quantity_of_categories\
     import calculate_quantity_of_categories


def top_5_categories():
    news_list = find_news()
    news_categories = [news["category"] for news in news_list]
    categories_quantity = calculate_quantity_of_categories(news_categories)
    sorted_categories = sorted(categories_quantity,
                               key=categories_quantity.get, reverse=True)
    return sorted_categories
