import sys

from api_utils import get_json

city = input("Type a city: ").strip()

params = {"name": city, "count": 1, "language": "sv"}

result = get_json("https://geocoding-api.open-meteo.com/v1/search", params)

if result and "results" in result:
    place = result["results"][0]
    latitude = place["latitude"]
    longitude = place["longitude"]
    print(f"{place['name']}, {place.get('country', '')}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}\n")

else:
    print(f"Could not find '{city}'.")
    sys.exit(1)

weather = get_json(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    },
)

print(
    f"Temperature: {weather['current']['temperature_2m']}{weather['current_units']['temperature_2m']} Wind: {weather['current']['wind_speed_10m']} km/h"
)
