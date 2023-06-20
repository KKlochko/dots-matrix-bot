import simplematrixbotlib as botlib
import aiohttp
import asyncio
import ujson
from src.config.dots_bot_api_config import DotsBotApiConfig

from src.api.v2.category_api import CategoryAPI
from src.fetcher.v2.api_fetcher import ApiFetcher
from src.fmt.category_formatter import CategoryFormatter

dots_bot_api_config = DotsBotApiConfig()

async def category_list_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str):

    session = aiohttp.ClientSession(json_serialize=ujson.dumps)
    apiFetcher = ApiFetcher(dots_bot_api_config.get_base_url(), session)
    formatter = CategoryFormatter()
    categoryAPI = CategoryAPI(apiFetcher, formatter)

    msg: str = await categoryAPI.get_objects_message(sender)

    await bot.api.send_markdown_message(room_id=room_id, message=msg)

