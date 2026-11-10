import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 48.85, "longitude": 2.35, "current": "temperature_2m"},
    timeout=10,
)
response.raise_for_status()      # raises an error on 4xx/5xx
data = response.json()
print(data["current"]["temperature_2m"])