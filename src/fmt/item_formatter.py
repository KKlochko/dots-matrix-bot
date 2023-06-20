from src.fmt.abstract_formatter import AbstractFormatter

class ItemFormatter(AbstractFormatter):
    def format(self, item) -> str:
        name = item['name']
        price = item['price']
        return f"- {name} - {price} ₴\n"

    def format_all(self, items: dict, header: str = "") -> str:
        formated_message = header

        items = items['data'] if 'data' in items else items
        
        for item in items:
            formated_item = self.format(item)
            formated_message += formated_item

        return formated_message

