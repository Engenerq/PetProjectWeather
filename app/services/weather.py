from fastapi import Depends

from app.models.weather import GetWeatherByCity, WeatherResponse
from app.repository.weather import WeatherRepository


class WeatherService:
    def __init__(self, repo: WeatherRepository = Depends(WeatherRepository)):
        self.repo = repo

    async def get_weather(self, data: GetWeatherByCity) -> WeatherResponse:
        """
        Запрос погоды в населенном пункте
        :param data: модель с данными для запроса
        :return: возвращает заполненную модель от репозитория
        """

        return await self.repo.get_weather(data)
