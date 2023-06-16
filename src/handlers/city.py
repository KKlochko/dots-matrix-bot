import simplematrixbotlib as botlib
import aiohttp
import asyncio
import ujson

from src.api.v2.city_api import CityAPI
from src.fetcher.v2.api_fetcher import ApiFetcher
from src.fmt.city_formatter import CityFormatter

async def list_cities_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str):

    session = aiohttp.ClientSession(json_serialize=ujson.dumps)
    apiFetcher = ApiFetcher("https://domain", session)
    formatter = CityFormatter()
    cityAPI = CityAPI(apiFetcher, formatter)

    msg: str = await cityAPI.get_objects_message()

    await bot.api.send_markdown_message(room_id=room_id, message=msg)

