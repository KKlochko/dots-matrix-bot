import pytest
from src.fmt.city_formatter import CityFormatter

def test_city_format():
    city = {'name': 'Chernihiv'}

    formatter = CityFormatter()

    city_fmt = formatter.format(city)

    assert '- Chernihiv\n' == city_fmt

def test_format_cities():
    cities = {'data': [
        {'name': 'Київ'},
        {'name': 'Чернігів'}
    ]}

    expected_format = "".join([
        "# Міста\n\n",
        "- Київ\n",
        "- Чернігів\n",
    ])

    formatter = CityFormatter()

    cities_fmt = formatter.format_all(cities)

    assert expected_format == cities_fmt

