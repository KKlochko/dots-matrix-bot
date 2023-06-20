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

