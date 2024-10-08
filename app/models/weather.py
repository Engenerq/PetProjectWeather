import re
from pydantic import BaseModel, model_validator


class GetWeatherByCity(BaseModel):
    """
    Параметры запроса погоды по городу
    """

    city: str

    @model_validator(mode="after")
    def city_english(self) -> "GetWeatherByCity":
        """
        Валидатор названия города
        :return: возвращает город
        """
        if not re.match(r"^[a-zA-Z]+$", self.city):
            raise ValueError("Город должен состоять из английских букв")
        return self


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
        cls.temp = response["main"]["temp"]
        cls.pressure = response["main"]["pressure"]
        cls.wind_speed = response["wind"]["speed"]

        return cls
