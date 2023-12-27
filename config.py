import logging.config
import os
from pathlib import Path

# Project config
root = Path(__file__).parent

# Openweathermap config
WEATHER_API_KEY = '3f28da7670af3217749b221251191780'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}

# Telegram  bot config
TG_TOKEN = '6665661351:AAEpVe2kT-E6adSKA34eyGgx1Jx475aoRIQ'
notify_timeout = 60 * 10  # in seconds
max_notify_cities_for_user = 5

# Logging config
aiogram_logging_level = logging.INFO
matplotlib_logging_level = logging.WARN
logging.config.fileConfig(f'{root}/logging.conf', disable_existing_loggers=False)
logging.getLogger('aiogram').setLevel(aiogram_logging_level)
logging.getLogger('matplotlib').setLevel(matplotlib_logging_level)
