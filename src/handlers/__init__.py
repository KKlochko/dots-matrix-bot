import nio
import simplematrixbotlib as botlib

from src.handlers.help import help_handler
from src.handlers.city import city_list_handler, select_city_handler
from src.handlers.company import company_list_handler, select_company_handler
from src.handlers.category import category_list_handler
from src.handlers.cart import cart_list_handler, add_item_handler
from src.handlers.cart import order_handler
from src.handlers.user import register_handler

from src.fmt.city_formatter import CityFormatter
from src.fmt.company_formatter import CompanyFormatter

def setup(bot: botlib.Bot, prefix: str):
    @bot.listener.on_message_event
    async def help_command(room: nio.rooms.MatrixRoom, message: nio.events.room_events.Event):
        match = botlib.MessageMatch(room, message, bot, prefix=prefix)

        if not match.is_not_from_this_bot():
            return

        if not match.prefix():
            return

        # No registered user required

        if match.command('help'):
            await help_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.command('city-list'):
            await city_list_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.command('select-city'):
            formatter = CityFormatter()
            city_name = formatter.get_name_from_parts(match.args())
            await select_city_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id, city_name=city_name)

        if match.command('register'):
            await register_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id, args=match.args())

        # A registered user required

        if match.command('company-list'):
            await company_list_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.command('select-company'):
            formatter = CompanyFormatter()
            company_name = formatter.get_name_from_parts(match.args())
            await select_company_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id, company_name=company_name)

        if match.command('category-list'):
            await category_list_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.command('cart'):
            await cart_list_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.command('add-item'):
            formatter = CompanyFormatter()
            line = formatter.get_name_from_parts(match.args())

            name, count = line.split(',')
            count = int(count)
            await add_item_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id, item_name=name, count=count)

        if match.command('order'):
            await order_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

