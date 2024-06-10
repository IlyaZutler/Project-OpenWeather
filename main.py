from weather_lib import *
import weather_lib as wlib
import streamlit as st

url = "https://raw.githubusercontent.com/IlyaZutler/Project-OpenWeather/main/param_defolt.json"

defolt_parametrs = wlib.get_defolt_parametrs(url)
city = defolt_parametrs['params']['city']
units = defolt_parametrs['params']['units']
key = defolt_parametrs['params']['key']
hi = defolt_parametrs['welcome']['hi']


st.title('OpenWeather Forecast')
st.write(hi)
city = st.text_input('Enter the city (if necessary, add country code separated by comma): ', city)
if st.button('Show Weather'):
    data = wlib.get_weather(city, units, key)
    if not data:
        st.write('Something is going wrong......')
    else:
        dt_txt_datetime, temp, temp_min, temp_max, humidity, description = wlib.data_to_lists(data)
        sunrise, sunset = wlib.get_sun_time(data)
        local_time = wlib.time_in_the_city(data)
        city = data['city']['name'] + ' ' + data['city']['country']

        st.write(f'Time in the {city}:  {local_time.strftime("%H:%M     %d.%m.%Y")}')
        st.write(f'Sunrise:      {sunrise.strftime("%H:%M")}')
        st.write(f'Sunset:       {sunset.strftime("%H:%M")}')
        st.write(f'Temperature Now:  from {temp_min[0]:.1f}  to {temp_max[0]:.1f} °C')
        st.write(f'Weather Now:      {description[0]}')
        st.write(f'Humidity Now:     {humidity[0]} %')
        df = wlib.make_df_for_streamlit(dt_txt_datetime, temp)
        st.line_chart(df)
        # data_with_grid = df.style.set_properties(**{'background-color': 'rgba(0, 0, 0, 0.1)', 'color': 'black'})
        # st.line_chart(data_with_grid, use_container_width=True)

        st.dataframe(table_of_data(dt_txt_datetime, temp_min, temp_max, humidity, description))
