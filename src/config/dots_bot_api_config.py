class DotsBotApiConfig():
    _base_url = "https://domain"

    def __str__(self) -> str:
        return f"{self._base_url=}"

    def get_base_url(self) -> str:
        return self._base_url

