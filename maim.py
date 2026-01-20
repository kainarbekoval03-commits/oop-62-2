# Библиотека: requests
# Назначение: удобная работа с HTTP-запросами (GET, POST и др.)
# Используется для получения данных из API, сайтов, микросервисов

import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())