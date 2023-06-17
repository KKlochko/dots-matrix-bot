import simplematrixbotlib as botlib
import aiohttp
import asyncio
import ujson
from src.config.dots_bot_api_config import DotsBotApiConfig

from src.api.v2.user_api import UserAPI
from src.fetcher.v2.api_fetcher import ApiFetcher

dots_bot_api_config = DotsBotApiConfig()

async def register_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str, args):
    count = len(args)

    if count == 0:
        await bot.api.send_markdown_message(room_id=room_id, message=
                                            """
Введіть Ім'я користувача, username та телефон 380?????????.
Приклад: `!register username 380671231212`.
                                            """)
        return

    session = aiohttp.ClientSession(json_serialize=ujson.dumps)
    apiFetcher = ApiFetcher(dots_bot_api_config.get_base_url(), session)
    userAPI = UserAPI(apiFetcher, None)

    username, phone = args[0], args[1]
    msg: str = await userAPI.register_user_message(username, sender, phone)

    await bot.api.send_markdown_message(room_id=room_id, message=msg)

