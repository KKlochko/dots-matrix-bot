from src.fmt.city_formatter import CityFormatter

class CompanyFormatter(CityFormatter):
    def format_all(self, companies: dict, header: str = "# Компанії\n\n") -> str:
        formated_message = header

        for company in companies['data']:
            formated_item = self.format(company)
            formated_message += formated_item

        return formated_message

