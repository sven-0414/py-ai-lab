import os
import requests
from dotenv import load_dotenv
from api_utils import get_json


load_dotenv()
api_key = os.getenv("API_KEY")
params = {"sort": "pushed", "per_page": 5}
headers = {"Authorization": f"Bearer {api_key}"}

r = requests.get("https://api.github.com/users/sven-0414/repos")

print("Status:", r.status_code)
print("Limit:", r.headers.get("X-RateLimit-Limit"))
print("Remaining:", r.headers.get("X-RateLimit-Remaining"))

result = get_json(
    "https://api.github.com/users/sven-0414/repos",
    params=params,
    headers=headers,
)

print(result)
