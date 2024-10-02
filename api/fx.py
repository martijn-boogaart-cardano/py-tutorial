import datetime as dt
import random
from time import sleep
from typing import Any

from api.core import parse_error, parse_response

__cache: dict[str, int] = {
    "PortfolioA2": 20,
    "PortfolioB2": 220,
    "PortfolioD3": 70
}


def get_all() -> dict[str, Any]:
    sleep(1)
    result = list(__cache.keys())
    return parse_response(result)


def get_portfolio(portfolio: str, date: dt.date) -> dict[str, Any]:
    sleep(10)
    if not _is_request_valid(portfolio, date):
        return parse_error(f"Invalid portfolio {portfolio} or date {date}.")

    random.seed(10_000 * date.year + 100 * date.month + date.day)
    alpha = random.random() + 1

    result = int(__cache[portfolio] * alpha)
    return parse_response(result)


def _is_request_valid(portfolio: str, date: dt.date) -> bool:
    if portfolio not in __cache:
        return False

    return date <= dt.date.today()
