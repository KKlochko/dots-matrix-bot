import pytest
from src.fmt.category_formatter import CategoryFormatter

def test_category_format():
    category = {
        'name': 'Напої'
    }

    formatter = CategoryFormatter()

    category_fmt = formatter.format(category)

    assert '#### Напої\n' == category_fmt

def test_format_categories_with_no_items():
    categories = {'data': [
        {'name': 'Піци'},
        {'name': 'Напої'},
    ]}

    expected_format = "".join([
        "# Категорії\n\n",
        "#### Піци\n",
        "#### Напої\n",
    ])

    formatter = CategoryFormatter()

    categories_fmt = formatter.format_all(categories)

    assert expected_format == categories_fmt

def test_format_categories_with_items():
    categories = {'data': [
        {
            'name': 'Піци',
            'items': [
                {
                    'name': 'Піца Поло',
                    'price': 99.99,
                },
                {
                    'name': 'Піца Чотири Сири',
                    'price': 89.99,
                },
            ]
        },
        {
            'name': 'Напої',
            'items': [
                {
                    'name': 'Чай',
                    'price': 39.99,
                },
                {
                    'name': 'Кава',
                    'price': 49.99,
                },
            ]
        },
    ]}

    expected_format = "".join([
        "# Категорії\n\n",
        "#### Піци\n",
        "- Піца Поло - 99.99 ₴\n",
        "- Піца Чотири Сири - 89.99 ₴\n",
        "#### Напої\n",
        "- Чай - 39.99 ₴\n",
        "- Кава - 49.99 ₴\n",
    ])

    formatter = CategoryFormatter()

    categories_fmt = formatter.format_all(categories)

    assert expected_format == categories_fmt

