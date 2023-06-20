import pytest
from src.fmt.company_formatter import CompanyFormatter

def test_company_format():
    company = {'name': 'Pizza company'}

    formatter = CompanyFormatter()

    company_fmt = formatter.format(company)

    assert '- Pizza company\n' == company_fmt

def test_format_companies():
    companies = {'data': [
        {'name': 'Pizza company'},
        {'name': 'Donuts company'}
    ]}

    expected_format = "".join([
        "# Компанії\n\n",
        "- Pizza company\n",
        "- Donuts company\n",
    ])

    formatter = CompanyFormatter()

    companies_fmt = formatter.format_all(companies)

    assert expected_format == companies_fmt

def test_get_name_from_one_parts():
    company_parts = ['Компанія']

    expected_name = 'Компанія'

    formatter = CompanyFormatter()

    company_name = formatter.get_name_from_parts(company_parts)

    assert expected_name == company_name

def test_get_name_from_two_parts():
    company_parts = ['Велика', 'компанія']

    expected_name = 'Велика компанія'

    formatter = CompanyFormatter()

    company_name = formatter.get_name_from_parts(company_parts)

    assert expected_name == company_name

