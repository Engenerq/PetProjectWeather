Реализовать API, которое на HTTP-запрос `GET /weather?city=<city_name>`,
где `<city_name>` - это название города на английском языке, 
возвращает текущую температуру в этом городе в градусах Цельсия, атомсферное давление (мм рт.ст.) и скорость ветра (м/c).
При первом запросе, сервис должен получать данные о погоде от openweathermap.com,
при последующих запросах для этого города в течение получаса запросы на сервис openweathermap.com происходить не должны.
Код должен быть выложен в открытом репозитории на github, содержать файл `requirements.txt` со списком зависимостей и инструкцию по запуску.