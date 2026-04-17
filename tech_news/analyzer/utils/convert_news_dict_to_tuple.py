def convert_news_dict_to_tuple(news_list: list):
    filtered_news = list()
    for news in news_list:
        curr_news = (news["title"], news["url"])
        filtered_news.append(curr_news)
    return filtered_news
