from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
# from tests.reading_plan.mocks.mocked_news import mocked_news
# from tests.reading_plan.mocks.response_mock import response_mock
import pytest
from unittest.mock import patch


def find_news_mock():
    return [
{'url': 'https://blog.betrybe.com/tecnologia/arquivo-bin/', 'title': 'Arquivo BIN: o que é, como abrir e converter?', 'timestamp': '22/06/2022', 'writer': 'Cairo Noleto', 'reading_time': 5, 'summary': 'Desde o surgimento do computador e seus respectivos softwares, em vários momentos nós já realizamos várias instalações de softwares para fins diversos, desde sistema operacional até videogames. Esse processo ocorre utilizando um arquivo BIN, que contém a cópia exata da base original do software, porém numa versão mais compacta e ocupando menos espaço de disco.', 'category': 'Tecnologia'},
{'url': 'https://blog.betrybe.com/noticias/axie-infinity-reabre-transacoes-apos-perder-bilhoes/', 'title': 'Axie Infinity reabre transações após perder R$3 bilhões', 'timestamp': '28/06/2022', 'writer': 'Allan Camilo', 'reading_time': 2, 'summary': 'Seja pelo sucesso ou pelo fracasso, Axie Infinity deu o que falar desde o ano passado, com a enorme quantia de dinheiro movimentada no mercado de NFTs. Agora, o grupo Sky Mavis (que cuida da marca) anunciou que os jogadores poderão voltar a usar a plataforma dedicada para realizar depósitos e saques.', 'category': 'Notícias'},
{'url': 'https://blog.betrybe.com/noticias/bill-gates-e-cetico-sobre-criptomoedas-e-nfts-entenda-o-motivo/', 'title': 'Bill Gates é cético sobre criptomoedas e NFTs', 'timestamp': '15/06/2022', 'writer': 'Allan Camilo', 'reading_time': 2, 'summary': 'Desde o ano passado, Bill Gates dá declarações espinhosas sobre a febre das criptomoedas. No final de 2021, houve bastante prejuízo ao mercado, seja pela queda do Bitcoin e do Ethereum, ou até por conta de invasores. “Se você tem menos dinheiro que Elon Musk, é melhor ter cuidado”, disse ele em entrevista ao Bloomberg.', 'category': 'Notícias'},
{'url': 'https://blog.betrybe.com/noticias/chatbots-entenda-os-problemas-de-relacionamentos-com-maquinas/', 'title': 'Chatbots: Entenda os problemas de relacionamentos com máquinas', 'timestamp': '30/06/2022', 'writer': 'Allan Camilo', 'reading_time': 6, 'summary': 'A empresa Replika, cuja sede fica na Califórnia (EUA), proporciona a seus clientes um chatbot criado especificamente para fazer companhia. Como contam neste curta documental do YouTube, os laços emocionais são criados a partir dessas interações, com o fator de “entretenimento” ganhando uma nova camada de intimidade.', 'category': 'Notícias'},
{'url': 'https://blog.betrybe.com/noticias/como-jogar-a-nova-temporada-de-fortnite-sem-download/', 'title': 'Como jogar a nova temporada de Fortnite sem download', 'timestamp': '07/06/2022', 'writer': 'Allan Camilo', 'reading_time': 10, 'summary': 'A terceira temporada do Capítulo 3 de Fortnite foi ao ar no último domingo (05), com novos itens, armas, um mapa remodelado e skins de Indiana Jones e Darth Vader. Como de costume, a temporada também traz um novo público interessado, somado ao modo Zero Construção, que resgata a jogabilidade tradicional dos Battle Royales. Porém, você precisa de pelo menos 35GB disponíveis, caso queira baixar o jogo gratuitamente pelo launcher da Epic Games.', 'category': 'Notícias'}
]


def test_reading_plan_group_news():
    with patch("tech_news.analyzer.reading_plan.find_news", find_news_mock):
        assert ReadingPlanService.group_news_for_available_time(5)\
             == {
    "readable": [
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "Arquivo BIN: o que é, como abrir e converter?",
                    5,
                ),
            ],
        },
        {
            "unfilled_time": 1,
            "chosen_news": [
                (
                    "Axie Infinity reabre transações após perder R$3 bilhões",
                    2,
                ),
                (
                    "Bill Gates é cético sobre criptomoedas e NFTs",
                    2,
                ),
            ],
        },
    ],
            "unreadable": [
        ("Chatbots: Entenda os problemas de relacionamentos com máquinas", 6),
        ("Como jogar a nova temporada de Fortnite sem download", 10),
    ],
        }

        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(0)
