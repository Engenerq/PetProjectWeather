from pydantic import BaseModel


class GetWeatherByCity(BaseModel):
    """
    Выдать погоду по названию города(eng)
    """

    city: str


class WeatherResponse(BaseModel):
    """
    Ответ на запрос
    """

    temp: float
    pressure: float
    wind_speed: float
