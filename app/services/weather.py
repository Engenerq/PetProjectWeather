from fastapi import Depends

from app.models.weather import GetWeatherByCity, WeatherResponse
from app.repository.weather import WeatherRepository


class WeatherService:
    def __init__(self, repo: WeatherRepository = Depends(WeatherRepository)):
        self.repo = repo

    async def get_weather(self, data: GetWeatherByCity) -> WeatherResponse:
        """
        Вернуть погоду по названию городу
        :return:
        """

        return await self.repo.get_weather(data)
