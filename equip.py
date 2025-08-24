import requests
import os


url = "https://api.artifactsmmo.com/my/Heisenberg/action/equip"
token = os.getenv('API_TOKEN')

payload = {
    "code": "wooden_staff",
    "slot": "weapon",
}


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}


response = requests.post(url, json=payload, headers=headers)
print(response.json())