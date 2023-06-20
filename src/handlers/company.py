import simplematrixbotlib as botlib
import aiohttp
import asyncio
import ujson
from src.config.dots_bot_api_config import DotsBotApiConfig

from src.api.v2.company_api import CompanyAPI
from src.fetcher.v2.api_fetcher import ApiFetcher
from src.fmt.company_formatter import CompanyFormatter

dots_bot_api_config = DotsBotApiConfig()

async def company_list_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str):

    session = aiohttp.ClientSession(json_serialize=ujson.dumps)
    apiFetcher = ApiFetcher(dots_bot_api_config.get_base_url(), session)
    formatter = CompanyFormatter()
    companyAPI = CompanyAPI(apiFetcher, formatter)

    msg: str = await companyAPI.get_objects_message(sender)

    await bot.api.send_markdown_message(room_id=room_id, message=msg)

async def select_company_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str, company_name: str):

    session = aiohttp.ClientSession(json_serialize=ujson.dumps)
    apiFetcher = ApiFetcher(dots_bot_api_config.get_base_url(), session)
    formatter = CompanyFormatter()
    companyAPI = CompanyAPI(apiFetcher, formatter)

    msg: str = await companyAPI.select_object_message(company_name, sender)

    await bot.api.send_markdown_message(room_id=room_id, message=msg)

