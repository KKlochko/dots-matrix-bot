import pytest
from src.fmt.item_formatter import ItemFormatter

def test_item_format():
    item = {
        'name': 'Піца',
        'price': 99.99,
    }

    formatter = ItemFormatter()

    item_fmt = formatter.format(item)

    assert '- Піца - 99.99 ₴\n' == item_fmt

def test_format_items():
    items = {'data': [
        {
            'name': 'Піца',
            'price': 99.99,
        },
        {
            'name': 'Чай',
            'price': 9.99,
        },
    ]}

    expected_format = "".join([
        '- Піца - 99.99 ₴\n',
        '- Чай - 9.99 ₴\n',
    ])

    formatter = ItemFormatter()

    items_fmt = formatter.format_all(items)

    assert expected_format == items_fmt

def test_get_name_and_count_from_parts():
    name_and_count = 'Дуже довга назва страви, 10'

    expected_name = 'Дуже довга назва страви'
    expected_count = 10

    formatter = ItemFormatter()

    item = formatter.get_name_and_count_from_parts(name_and_count)
    item_name, item_count = item['name'], item['count']

    assert expected_name == item_name
    assert expected_count == item_count

def test_get_name_and_count_from_parts_invalid_command():
    name_and_count = 'Дуже довга назва страви 10'

    formatter = ItemFormatter()

    error = formatter.get_name_and_count_from_parts(name_and_count)

    assert 'Не правильний формат' == error['error']

