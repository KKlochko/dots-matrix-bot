from src.fmt.abstract_formatter import AbstractFormatter

class CityFormatter(AbstractFormatter):
    def format(self, city) -> str:
        name = city['name']
        return f"- {name}\n"

    def format_all(self, cities: dict) -> str:
        formated_message = "Cities:\n\n"

        for city in cities['data']:
            formated_item = self.format(city)
            formated_message += formated_item

        return formated_message

