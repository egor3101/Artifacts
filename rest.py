import requests
import os

url = "https://api.artifactsmmo.com/my/Heisenberg/action/rest"
token = os.getenv('API_TOKEN')

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.post(url, headers=headers)

print(response.json())