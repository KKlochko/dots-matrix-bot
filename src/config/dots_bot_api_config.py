from environs import Env

env = Env()
env.read_env()

class DotsBotApiConfig():
    _base_url = env('BOT_API_BASE_URL')

    def __str__(self) -> str:
        return f"{self._base_url=}"

    def get_base_url(self) -> str:
        return self._base_url

