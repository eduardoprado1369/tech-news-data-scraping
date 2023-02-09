def convert_news_dict_to_tuple(news_dict: dict):
    news_list = list()
    for news in news_dict:
        curr_news = (news["title"], news["url"])
        news_list.append(curr_news)
    return news_list
