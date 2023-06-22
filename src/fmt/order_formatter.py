
class OrderFormatter():
    def format(self, order) -> str:
        id = order['id']
        order_type = order['delivery']['deliveryTypeText']
        order_address = order['delivery']['deliveryAddress']
        item_price = order['prices']['itemsPrice']
        package_price = order['prices']['packagePrice']
        delivery_price = order['prices']['deliveryPrice']
        full_price = order['prices']['fullPrice']
        return f"Ваше замовлення має id: {id}.\n" \
               f"Вид доставки: {order_type}.\n" \
               f"Доставка до: {order_address}.\n" \
               f"Ціна товарів: {item_price}.\n" \
               f"Ціна пакування: {package_price}.\n" \
               f"Ціна доставки: {delivery_price}.\n\n" \
               f"Остаточна ціна: {full_price}."

