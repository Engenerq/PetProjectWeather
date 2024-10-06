from app.models.weather import WeatherResponse, GetWeatherByCity
from requests import get
from dotenv import dotenv_values


class WeatherRepository:
    model = WeatherResponse

    async def get_weather(self, payload: GetWeatherByCity) -> model:
        """
        Запрос о погоде на сервис openweather
        :payload: город(eng)
        :return:
        """

        req = get(
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={payload.city}&"
            f"units=metric"
            f"&lang=ru&"
            f"appid={dotenv_values()['TOKEN']}").json()

        data = self.model(temp=req["main"]["temp"],
                          pressure=req["main"]["pressure"],
                          wind_speed=req["wind"]["speed"])

        return data
