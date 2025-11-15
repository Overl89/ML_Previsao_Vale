import requests

url = "https://lucivando-docker.hf.space/fechamento"
payload = {"date": "2025-11-20"}

response = requests.post(url, json=payload)
print(response.json())

