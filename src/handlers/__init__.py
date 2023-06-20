import nio
import simplematrixbotlib as botlib

from src.handlers.help import help_handler
from src.handlers.city import list_cities_handler, select_city_handler
from src.handlers.user import register_handler

from src.fmt.city_formatter import CityFormatter

def setup(bot: botlib.Bot, prefix: str):
    @bot.listener.on_message_event
    async def help_command(room: nio.rooms.MatrixRoom, message: nio.events.room_events.Event):
        match = botlib.MessageMatch(room, message, bot, prefix=prefix)

        if not match.is_not_from_this_bot():
            return

        if not match.prefix():
            return

        if match.command('help'):
            await help_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.command('cities-list'):
            await list_cities_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.command('select-city'):
            formatter = CityFormatter()
            city_name = formatter.get_name_from_parts(match.args())
            await select_city_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id, city_name=city_name)

        if match.command('register'):
            await register_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id, args=match.args())

