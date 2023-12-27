import datetime
import time

import matplotlib.pyplot as plt

from config import root

weather_types = {
    "Clear": "Ясно \U00002600",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U00002614",
    "Drizzle": "Дождь \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U0001F32B"
}


def convert_to_celsius(num: float | int) -> float:
    return round(num - 273.15, 2)


def get_msg_from_raw_weather_data(data: dict, city: str) -> str:
    current_temp = convert_to_celsius(int(data['main']['temp']))
    weather_type = data['weather'][0]['main']
    if weather_type in weather_types:
        weather_type = weather_types[weather_type]
    else:
        weather_type = 'Апокалипсис!'
    humidity = data['main']['humidity']
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    msg = (f'<b>{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}</b>\n'
           f'\n'
           f'<b>Город:</b> {city}\n'
           f'<b>Температура:</b> {current_temp}C° {weather_type}\n'
           f'<b>Влажность:</b> {humidity}%\n'
           f'<b>Давление:</b> {pressure} мм.рт.ст\n'
           f'<b>Ветер:</b> {wind} м/с\n'
           f'<b>Восход солнца:</b> {sunrise_timestamp.strftime("%H:%M:%S")}\n'
           f'<b>Закат солнца:</b> {sunset_timestamp.strftime("%H:%M:%S")}\n'
           f'<b>Продолжительность дня:</b> {sunset_timestamp - sunrise_timestamp}')
    return msg


def get_ticks_and_labels(raw_dates):
    ticks, labels = [], []
    for i, date in enumerate(raw_dates):
        if "00:00:00" in date:
            ticks.append(i)
            labels.append(date.split(' ')[0])
    ticks.append(2 * ticks[-1] - ticks[-2])
    labels.append(str(datetime.datetime.fromisoformat(raw_dates[-1]) + datetime.timedelta(days=1)).split(' ')[0])
    return ticks, labels


def create_plot_from_weather_data(weather_data: dict, city: str) -> str:
    temperatures = []
    raw_dates = []
    for dt in weather_data['list']:
        date = dt['dt_txt']
        raw_dates.append(date)
        temperatures.append(convert_to_celsius(dt['main']['temp']))
    fig, ax = plt.subplots()

    ticks, labels = get_ticks_and_labels(raw_dates)

    plt.xticks(ticks, labels)

    fig.autofmt_xdate()
    ax.plot(raw_dates, temperatures, '-o')
    ax.set_title(f'График температуры на 5 дней в городе {city}')
    plt.xlabel('Дата')
    plt.ylabel('Температура (C°)')
    plt.grid(True)
    fig.show()
    file_path = f'{root}/weatherBot/plots/{time.time()}.jpeg'
    fig.savefig(file_path)
    return file_path
