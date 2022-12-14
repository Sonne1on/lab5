import requests
import json

from config_key import key


def res_weather(city_name, key):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric")
    r = res.json()
    city_name = r['name']
    temp_min = r['main']['temp_min'] # Температура ночью
    temp_max = r['main']['temp_max'] # Температура днем
    hum = r['main']['humidity'] # Влажность
    press = round((r['main']['pressure'] * 100)/132) # Давление

    print(f"{city_name} \n"
          f"Температура (в градусах Цельсия): {temp_min} - {temp_max} \n"
          f"Влажность (%):                    {hum}\n"
          f"Давление (мм рт/ст):              {press}")


def city_name():
    city_name = input("Введите название города: \n")
    res_weather(city_name, key)

city_name()
print('________________________________________________')


def open_hh():

    print("Вариант 1. - hh.ru \n")
    res = requests.get("https://api.hh.ru/vacancies")
    res_t = requests.get("https://api.hh.ru/vacancies").text

    data = json.loads(res_t)# преобразуем Json

    print('1:  ', res)# Проверяем запрос на ошибку
    print('2:  ', type(res_t))
    print('3:  ', data)
    print('4:  ', type(data))


open_hh()
print('________________________________________________
