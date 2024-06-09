
import datetime
from datetime import timedelta
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

def get_defolt_parametrs(url):
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def get_weather(city, units, key):
    api_url = "http://api.openweathermap.org/data/2.5/forecast"

    response = requests.get(api_url, params={"q": city, "units": units, "appid": key})
    if response.status_code == 200:
        return response.json()
    else:
        return None

def data_to_lists(data):
    dt_txt = []
    temp = []
    temp_min = []
    temp_max = []
    humidity = []
    description = []
    for i in range(len(data['list'])):
        dt_txt.append(data['list'][i]['dt_txt'])
        temp.append(round(data['list'][i]['main']['temp'], 1))
        temp_min.append(round(data['list'][i]['main']['temp_min'], 1))
        temp_max.append(round(data['list'][i]['main']['temp_max'], 1))
        humidity.append(data['list'][i]['main']['humidity'])
        description.append(data['list'][i]['weather'][0]['description'])

    # Convert dt_txt to datetime objects
    dt_txt_datetime = []
    for date_str in dt_txt:
        dt_txt_datetime.append(datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S'))

    return dt_txt_datetime, temp, temp_min, temp_max, humidity, description

def plot_weather(dt_txt_datetime, temp, city):

    # Extract month, day, and hour from datetime objects
    day_month_hour = []
    for time_obs in dt_txt_datetime:
        day_month_hour.append(f'{time_obs.day}.{time_obs.month}  {time_obs.hour}:00')

    plt.figure(figsize=(15, 5))
    plt.plot(day_month_hour, temp)
    plt.xlabel('Day - Month - Hour')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Forecast for {city}')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def time_in_the_city(data):
    city_timezone = data['city']['timezone']
    utc_now = datetime.datetime.utcnow()
    local_time = utc_now + datetime.timedelta(seconds = city_timezone)
    return local_time

def get_sun_time(data):
    sunrise = datetime.datetime.fromtimestamp(data['city']['sunrise'] + data['city']['timezone'], datetime.timezone.utc)
    sunset = datetime.datetime.fromtimestamp(data['city']['sunset'] + data['city']['timezone'], datetime.timezone.utc)
    return sunrise, sunset

def table_of_data(dt_txt_datetime, temp_min, temp_max, humidity, description):
# Create a dictionary with the data
    day_month_hour = []
    for time_obs in dt_txt_datetime:
        day_month_hour.append(time_obs.strftime("%d.%m.%Y    %H:%M"))

    tabla = {
        'day_time': day_month_hour,
        'temp_min °C': temp_min,
        'temp_max °C': temp_max,
        'humidity %': humidity,
        'weather': description
    }
    df =  pd.DataFrame(tabla)
    df.set_index('day_time', inplace = True)
    return df

def make_df_for_streamlit(dt_txt_datetime, temp):
    day_month_hour = []
    for time_obs in dt_txt_datetime:
        day_month_hour.append(time_obs.strftime("%d.%m    %H:%M"))

    tabla = {
        'day_time': day_month_hour,
        'temp': temp
    }
    df =  pd.DataFrame(tabla)
    df.set_index('day_time', inplace = True)
    return df
