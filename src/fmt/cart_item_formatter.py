from src.fmt.abstract_formatter import AbstractFormatter

class CartItemFormatter(AbstractFormatter):
    def format(self, item) -> str:
        fmt, _ = self.format_and_sum(item)

        return fmt

    def format_and_sum(self, item) -> (str, float):
        name = item['name']
        price = float(item['price'])
        count = float(item['count'])
        total_price = price*count

        return f"- {name} {count}x{price} ₴\n", total_price

    def format_all(self, items: dict, header: str = "# Кошик\n\n") -> str:
        total_sum = 0

        formated_message = header

        items = items['data'] if 'data' in items else items

        for item in items:
            formated_item, item_sum = self.format_and_sum(item)
            formated_message += formated_item
            total_sum += item_sum

        formated_message += f"#### Сума: {total_sum} ₴"

        return formated_message

