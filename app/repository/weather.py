import httpx

from app.config import get_settings
from app.models.weather import WeatherResponse, GetWeatherByCity

settings = get_settings()


class WeatherRepository:
    model = WeatherResponse

    async def get_weather(self, payload: GetWeatherByCity) -> model:
        """
        Запрос на сервис openweather
        :payload: модель с параметрами запроса
        :return: возвращает заполненную модель WeatherResponse
        """

        params = {"lang": "ru",
                  "units": "metric",
                  "q": f"{payload.city}",
                  "appid": settings.token_weather}

        req_for_openweather = "https://api.openweathermap.org/data/2.5/weather?"

        async with httpx.AsyncClient() as client:
            data = await client.get(req_for_openweather, params=params)
            return self.model.from_response(data.json())
