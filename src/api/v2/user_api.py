import aiohttp
import asyncio
import ujson

class UserAPI:
    def __init__(self, fetcher, formatter):
        """
        Sets needed classes:

        Fetcher (ApiFetcher) - class that will fetch data.
        Format  (AbstractFormat) - class that will format response data.
        """
        self.__fetcher, self.__formatter = fetcher, formatter

    async def register(self, username: str, matrix_username: str, phone: str):
        endpoint = "/api/v2/register"

        status, json_data = await self.__fetcher.send_json(endpoint, {
            'username': username,
            'matrixUsername': matrix_username,
            'phone': phone,
        })

        if status != 200:
            return {"error": "Сталася помилка, спробуйте пізніше."}

        match json_data:
            case {"ok": message}:
                return {"ok": 'Користувач успішно створений.'}
            case {"error": 'A user with the username already exists!!!'}:
                return {"error": "Користувач вже існує, будь ласка, оберіть інше ім'я"}
            case {"error": error_message}:
                return {"error": error_message}


    async def register_user_message(self, username: str, matrix_username: str, phone: str) -> str:
        response = await self.register(username, matrix_username, phone)

        match response:
            case {"ok": message}:
                return message

            case {"error": error_message}:
                return error_message

