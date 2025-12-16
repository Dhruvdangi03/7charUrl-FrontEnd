import requests
from config.settings import settings

class URLService:

    @staticmethod
    def shorten(url: str):
        r = requests.post(
            f"{settings.API_BASE_URL}/shorten",
            json={"url": url},
            timeout=5
        )
        return r.json(), r.status_code

    @staticmethod
    def custom(url: str, custom: str):
        r = requests.post(
            f"{settings.API_BASE_URL}/custom",
            json={"url": url, "custom": custom},
            timeout=5
        )
        return r.json(), r.status_code
