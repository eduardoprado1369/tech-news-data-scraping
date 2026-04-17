from tech_news.analyzer.utils.convert_news_dict_to_tuple\
    import convert_news_dict_to_tuple


def filter_news(news_list: list, field: str, value: str):
    filtered_news = [news for news in news_list if value.lower()
                     in news[field].lower()]
    return convert_news_dict_to_tuple(filtered_news)
