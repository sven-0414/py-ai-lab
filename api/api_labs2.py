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
    print(f"Longitude: {longitude}")
else:
    print(f"Could not find '{city}'.")
