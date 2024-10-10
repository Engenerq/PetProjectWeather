import json
import re
from pydantic import BaseModel, field_validator


class GetWeatherByCity(BaseModel):
    """
    Параметры запроса
    """

    city: str

    @field_validator("city")
    @classmethod
    def city_english(cls, value: str):
        """
        Валидатор названия города
        :return: возвращает город
        """
        if not re.match(r"^[a-zA-Z]+$", value):
            raise ValueError("Город должен состоять из английских букв")
        return value


class WeatherResponse(BaseModel):
    """
    Параметры данных о погоде
    """

    temp: float
    pressure: float
    wind_speed: float

    @classmethod
    def from_response(cls, response) -> "WeatherResponse":
        """
        Заполнение модели WeatherResponse
        :param response: ответ от сервиса в формате json
        :return: возвращает заполненную модель WeatherResponse
        """

        return cls(temp=response["main"]["temp"],
                   pressure=response["main"]["pressure"],
                   wind_speed=response["wind"]["speed"]
                   )
