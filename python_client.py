import requests

url = "http://localhost:8000/api/"

json_ = {
    "patient_id": "P82395",
    "date": "2024-10-29",
    "age": 45,
    "sex": "Male",
    "occupation": "Software Engineer",
    "marital_status": "Married",
    "address": "47 Maple Avenue, Springfield",
    "religion": "Christianity",
    "tribe": "Igbo"
}


response = requests.post(url, json=json_)
response.raise_for_status
print(response.json())