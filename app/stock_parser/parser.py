from .models import Stocks
from .services.parsing_service.pars_service import format_number, get_price
from .services.parsing_service.pars_config import *


def create_data(category, stock_category):
    result_arr = []
    for stock in stock_category:
        price_arr = get_price(stock['name'], stock['url'], stock['xpath'], stock['xpath_proc'])
        result_arr.append(price_arr)

    for result in result_arr:
        formatted_value = float(format_number(result[1]))
        formatted_proc = format_number(result[2])
        proc_without_brackets = float(formatted_proc.replace("(", "").replace(")", ""))

        stock = Stocks(ticker=result[0],
                       category=category,
                       price=formatted_value,
                       change_percent=proc_without_brackets)
        Stocks.save_to_database(stock)


def parsing():
    print('Start app')
    create_data('Валюты', currencies)
    create_data('Товары', comodities)
    create_data('Индексы', index)
    print('All ok')


