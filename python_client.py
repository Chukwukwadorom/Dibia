import json
import requests
import os

# Base URL of your Django API server
BASE_URL = "http://127.0.0.1:8000/api" 

# Paths to the JSON files
data_files = {
    "patient.json": "patients",
    "vital.json": "vitals",
    "doctornote.json": "doctornotes",
}

# Function to read data from a JSON file
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to load data into the specified endpoint
def load_data(jsonpath, endpoint):
    url = f"{BASE_URL}/{endpoint}/"
    entries = read_json(f"jfiles/{jsonpath}")

    for data in entries:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print(f"Successfully added {jsonpath[:-5]} for patient {data}")
        else:
            print(f"Failed to add {jsonpath[:-5]} for patient {data}: {response.raise_for_status}")

# Main function to iterate over data files and load them
def main():
    for jsonpath, endpoint in data_files.items():
        load_data(jsonpath, endpoint)

if __name__ == "__main__":
    main()
