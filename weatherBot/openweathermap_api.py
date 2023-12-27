import logging

import requests

import config

logger = logging.getLogger('TGBot')


class Weather:
    def __init__(self, city, *, lon: float = None, lat: float = None):
        self.city = city
        self.__API_KEY = config.WEATHER_API_KEY
        self.lon = lon
        self.lat = lat

    def _get(self) -> dict | None:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.__API_KEY}"
        try:
            data = requests.get(url, headers=config.headers, timeout=10.0).json()
            return data
        except requests.exceptions.ReadTimeout:
            logger.warning('Some problem with openweathermap API')
            return None

    def get(self) -> dict | int:
        data = self._get()
        if data is None:
            return -1
        if data['cod'] == '404':
            return 0
        return data

    def get_forecast(self) -> dict | None:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.__API_KEY}"
        data = requests.get(url, headers=config.headers).json()
        return data
