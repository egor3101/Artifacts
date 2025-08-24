import requests
import os


url = "https://api.artifactsmmo.com/my/Heisenberg/action/crafting"
token = os.getenv('API_TOKEN')

payload = {
    "code": "wooden_staff"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())