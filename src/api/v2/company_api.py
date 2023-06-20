import aiohttp
import asyncio
import ujson

class CompanyAPI:
    def __init__(self, fetcher, formatter):
        """
        Sets needed classes:

        Fetcher (ApiFetcher) - class that will fetch data.
        Format  (AbstractFormat) - class that will format response data.
        """
        self.__fetcher, self.__formatter = fetcher, formatter

    async def get_dict(self, username: str):
        endpoint = f"/api/v2/companies?matrixUsername={username}"

        status, json_data = await self.__fetcher.fetch_json(endpoint)

        if status == 200:
            return {"ok": json_data}

        return {"error": "Сталася помилка, спробуйте пізніше."}

    async def select_obj(self, company_name: str, username: str):
        endpoint = "/api/v2/select-company"

        status, json_data = await self.__fetcher.send_json(endpoint, {
            'companyName': company_name,
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

    async def select_object_message(self, company_name: str, username: str) -> str:
        response = await self.select_obj(company_name, username)

        match response:
            case {"ok": json_data}:
                return 'Компанія обрана'

            case {"error": error_message}:
                return error_message

