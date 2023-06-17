import nio
import simplematrixbotlib as botlib

from src.handlers.help import help_handler
from src.handlers.city import list_cities_handler
from src.handlers.user import register_handler

def setup(bot: botlib.Bot, prefix: str):
    @bot.listener.on_message_event
    async def help_command(room: nio.rooms.MatrixRoom, message: nio.events.room_events.Event):
        match = botlib.MessageMatch(room, message, bot, prefix=prefix)

        if match.is_not_from_this_bot() and match.prefix() and match.command('help'):
            await help_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.is_not_from_this_bot() and match.prefix() and match.command('cities-list'):
            await list_cities_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

        if match.is_not_from_this_bot() and match.prefix() and match.command('register'):
            await register_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id, args=match.args())

