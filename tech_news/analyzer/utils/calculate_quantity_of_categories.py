def calculate_quantity_of_categories(news_categories):
    news_categories_sorted = sorted(news_categories)
    category_dict = dict()
    for category in news_categories_sorted:
        category_dict.update(
                {category: 0}
                )
    for name in news_categories_sorted:
        category_dict[name] += 1
    return category_dict
