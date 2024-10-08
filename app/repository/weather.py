from dotenv import dotenv_values
import httpx

from app.models.weather import WeatherResponse, GetWeatherByCity


class WeatherRepository:
    model = WeatherResponse

    async def get_weather(self, payload: GetWeatherByCity) -> WeatherResponse:
        """
        Запрос о погоде на сервис openweather
        :payload: модель с параметром city
        :return: возвращает модель WeatherResponse
        """

        req_for_openweather = (
            f"https://api.openweathermap.org/data/2.5/weather?lang=ru&units=metric&"
            f"q={payload.city}&"
            f"appid={dotenv_values()['TOKEN']}")

        async with httpx.AsyncClient() as client:
            data = await client.get(req_for_openweather)
            return self.model.from_response(data.json())
