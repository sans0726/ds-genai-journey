import requests

url = "http://127.0.0.1:5000/predict_api"

data = {
    "activity": 2,
    "area": 500,
    "common_flares": 2
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())