# Project OpenWeather

## Project Goal

The program is designed to provide weather information for the requested city. Upon request, the service provides information on:

- Local time in the city
- Sunrise and sunset times (important for planning sightseeing and welcoming Shabbat)
- Current temperature
- Weather conditions
- Humidity

Additionally, the service provides:
- A 5-day temperature forecast graph
- A table with extended 5-day weather forecast data

## Implementation

Weather information is obtained via the OpenWeatherMap API. The configuration settings are located in the `param_default.json` file. The utilized functions are stored in the library file `weather_lib.py`. The file `colab_weather_sh.ipynb` is used to run the program from Colab. The `main.py` file is used to run the program from the Streamlit service.

## Program Execution

The program can be executed via the following links:



Цель проекта

Программа предназначена для предоставления информации о погоде в запрашиваемом Городе.
По запросу сервис предоставляет информацию:
Локальное время в городе
Время восхода и захода солнца (важно для планирования осмотра достопримецательностей и встречи субботы) 
Текущую температуру 
Погодные условия
Влажность

График прогноза температуры на 5 дней
Таблицу с расширенными данными о прогнозе погоды на 5 днейю

Реализация

Информация о погоде получается по API от сервиса OpenWeatherMap.
Постоянные настройки размещены в файле param_defolt.json
Использованные функции вынесены в файл библиотеку weather_lib.py
Файл colab_weather_sh.ipynb для запуска программы из colab
Файл main.py используется для запуска с сервиса streamlit 


Запуск программ

программа запускается по ссылкам

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IlyaZutler/Project-OpenWeather/blob/main/colab_weather_sh.ipynb)

https://ds17-open-weather.streamlit.app/
