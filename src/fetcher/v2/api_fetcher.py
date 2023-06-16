import aiohttp
import asyncio
import ujson

class ApiFetcher:
    def __init__(self, base_url: str, session):
        self.__base_url = base_url
        self.__session = session

    async def fetch_json(self, endpoint: str) -> (int, dict):
        """
        Gets a JSON payload from the API endpoint.

        url (str): the JSON payload will be gotten to the URL.
        context (dict): the dictionary that will be sended as a JSON payload.
        """
        url = f"{self.__base_url}{endpoint}"

        async with self.__session.get(url) as response:
            status = response.status
            json_data = await response.json()
            return (status, json_data)

    async def send_json(self, endpoint: str, context: dict) -> (int, dict):
        """
        Sends a JSON payload to the API endpoint.

        url (str): the JSON payload will be sent to the API endpoint.
        context (dict): the dictionary that will be sent as a JSON payload.
        """
        url = f"{self.__base_url}{endpoint}"

        async with self.__session.get(url) as session:
            await session.post(url, json=context)
            json_data = await session.json()
            return (session.status, json_data)

