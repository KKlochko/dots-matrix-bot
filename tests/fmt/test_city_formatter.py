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

def test_get_name_from_one_parts():
    city_parts = ['Чернігів']

    expected_name = 'Чернігів'

    formatter = CityFormatter()

    city_name = formatter.get_name_from_parts(city_parts)

    assert expected_name == city_name

def test_get_name_from_two_parts():
    city_parts = ['Біла', 'Церква']

    expected_name = 'Біла Церква'

    formatter = CityFormatter()

    city_name = formatter.get_name_from_parts(city_parts)

    assert expected_name == city_name

