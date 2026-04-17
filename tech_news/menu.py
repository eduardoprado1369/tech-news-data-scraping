from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date,\
    search_by_category
from tech_news.analyzer.ratings import top_5_categories
import sys


# Requisitos 11 e 12.
def analyzer_menu():
    user_input = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair. """)
    return handle_input(user_input)


def handle_input(user_input: str):
    if user_input == '0':
        number_of_news_input = input(
            'Digite quantas notícias serão buscadas:')
        return get_tech_news(int(number_of_news_input))
    elif user_input == '1':
        title_input = input('Digite o título:')
        return search_by_title(title_input)
    elif user_input == '2':
        date_input = input('Digite a data no formato aaaa-mm-dd:')
        return search_by_date(date_input)
    elif user_input == '3':
        category_input = input('Digite a categoria:')
        return search_by_category(category_input)
    elif user_input == '4':
        return top_5_categories()
    elif user_input == '5':
        return print('Encerrando script')
    else:
        return print('Opção inválida', file=sys.stderr)
