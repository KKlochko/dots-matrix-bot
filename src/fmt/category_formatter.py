from src.fmt.abstract_formatter import AbstractFormatter
from src.fmt.item_formatter import ItemFormatter

class CategoryFormatter(AbstractFormatter):
    def format(self, category) -> str:
        name = category['name']
        return f"#### {name}\n"

    def format_all(self, cities: dict, header: str = "# Категорії\n\n") -> str:
        formated_message = header

        item_formatter = ItemFormatter()

        for category in cities['data']:
            formated_category = self.format(category)
            formated_message += formated_category

            if 'items' in category:
                formated_items = item_formatter.format_all(category['items'])
                formated_message += formated_items

        return formated_message

