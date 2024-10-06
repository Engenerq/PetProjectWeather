from fastapi import APIRouter, Depends

from app.models.weather import GetWeatherByCity, WeatherResponse
from app.services.weather import WeatherService

router_w = APIRouter(
    prefix="/weather",
    tags=["weather"],
)


@router_w.get("/",
              response_model=WeatherResponse,
              )
async def get_weather(
        payload: GetWeatherByCity = Depends(GetWeatherByCity),
        service: WeatherService = Depends(WeatherService),
):
    data = await service.get_weather(payload)

    return data
