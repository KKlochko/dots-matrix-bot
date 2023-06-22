import aiohttp
import asyncio
import ujson

class CartAPI:
    def __init__(self, fetcher, formatter):
        """
        Sets needed classes:

        Fetcher (ApiFetcher) - class that will fetch data.
        Format  (AbstractFormat) - class that will format response data.
        """
        self.__fetcher, self.__formatter = fetcher, formatter

    async def get_dict(self, username: str):
        endpoint = f"/api/v2/cart?matrixUsername={username}"

        status, json_data = await self.__fetcher.fetch_json(endpoint)

        if status == 200:
            return {"ok": json_data}

        return {"error": "Сталася помилка, спробуйте пізніше."}

    async def add_obj(self, item_name: str, count: int, username: str):
        endpoint = "/api/v2/add-item"

        status, json_data = await self.__fetcher.send_json(endpoint, {
            'itemName': item_name,
            'itemCount': count,
            'matrixUsername': username,
        })

        if status == 200:
            return {"ok": json_data}

        return {"error": "Сталася помилка, спробуйте пізніше."}

    async def get_objects_message(self, username: str) -> str:
        response = await self.get_dict(username)

        match response:
            case {"ok": json_data}:
                return self.__formatter.format_all(json_data)

            case {"error": error_message}:
                return error_message

    async def add_object_message(self, item_name: str, count: int, username: str) -> str:
        response = await self.add_obj(item_name, count, username)

        match response:
            case {"ok": json_data}:
                return 'Успішно додано'

            case {"error": error_message}:
                return error_message

    async def get_order(self, username: str):
        endpoint = f"/api/v2/order?matrixUsername={username}"

        status, json_data = await self.__fetcher.fetch_json(endpoint)

        if status == 200:
            return {"ok": json_data}

        return {"error": "Сталася помилка, спробуйте пізніше."}

    async def get_order_message(self, username: str) -> str:
        response = await self.get_order(username)

        match response:
            case {"ok": json_data}:
                return self.__formatter.format(json_data)

            case {"error": error_message}:
                return error_message

