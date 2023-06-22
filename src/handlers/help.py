import simplematrixbotlib as botlib


async def help_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str):
    msg: str = 'Привіт, **{}**\n\n' \
               'Префікс команда: `!`\n' \
               '[dots-matrix-bot](https://gitlab.com/KKlochko/dots-matrix-bot) - це вільне програмне забезпечення за лацензією GNU AGPLv3 чи будь-яка новіша версія.\n' \
               'Контакт адміна: **{}**\n\n' \
               '\n\nКоманди:\n' \
               'help - допомога.\n' \
               'register - пов\'язати користувача та акаунт матриці.\n' \
               'Приклад: `!register username 3806712312121`.\n\n' \
               'city-list - перелік міст.\n' \
               'company-list - перелік компаній.\n' \
               'category-list - перелік категорій та товарів.\n' \
               'cart - перелік товарів у кошику та їх вартість.\n\n' \
               'select-city - обрати місто.\n' \
               'Приклад: `!select-city Чернігів`.\n\n' \
               'select-company - обрати компанію.\n' \
               'Приклад: `!select-company Назва Компанії`.\n\n' \
               'add-item - додати товар у кошик.\n' \
               'Приклад: `!add-item !add-item Назва товару, 2`.\n\n' \
               'order - замовити.'

    await bot.api.send_markdown_message(room_id=room_id, message=msg.format(sender, admin_id))

