import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--x', type=int)
parser.add_argument('--y', type=int)
args = parser.parse_args()

token = os.getenv('API_TOKEN')

url = "https://api.artifactsmmo.com/my/Heisenberg/action/move"

payload = {
    "x": args.x,
    "y": args.y
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())