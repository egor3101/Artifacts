import requests
import os


url = "https://api.artifactsmmo.com/my/Heisenberg/action/unequip"
token = os.getenv('API_TOKEN')


payload = {
    "slot": "weapon",
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.post(url, json=payload, headers=headers)