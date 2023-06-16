import pytest
from src.fmt.city_formatter import CityFormatter

def test_city_format():
    city = {'name': 'Chernihiv'}

    formatter = CityFormatter()

    city_fmt = formatter.format(city)

    assert '- Chernihiv\n' == city_fmt

