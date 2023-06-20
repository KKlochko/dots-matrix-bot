import simplematrixbotlib as botlib
import aiohttp
import asyncio
import ujson
from src.config.dots_bot_api_config import DotsBotApiConfig

from src.api.v2.cart_api import CartAPI
from src.fetcher.v2.api_fetcher import ApiFetcher
from src.fmt.item_formatter import ItemFormatter
from src.fmt.cart_item_formatter import CartItemFormatter

dots_bot_api_config = DotsBotApiConfig()

async def cart_list_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str):

    session = aiohttp.ClientSession(json_serialize=ujson.dumps)
    apiFetcher = ApiFetcher(dots_bot_api_config.get_base_url(), session)
    formatter = CartItemFormatter()
    cartAPI = CartAPI(apiFetcher, formatter)

    msg: str = await cartAPI.get_objects_message(sender)

    await bot.api.send_markdown_message(room_id=room_id, message=msg)

async def add_item_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str, item_name: str, count: int):

    session = aiohttp.ClientSession(json_serialize=ujson.dumps)
    apiFetcher = ApiFetcher(dots_bot_api_config.get_base_url(), session)
    formatter = ItemFormatter()
    cartAPI = CartAPI(apiFetcher, formatter)

    msg: str = await cartAPI.add_object_message(item_name, count, sender)

    await bot.api.send_markdown_message(room_id=room_id, message=msg)

