import os

import requests

# Credentials
EMAIL = "lasse@woodsense.com"
PASSWORD = os.getenv("WOODSENSE_PASSWORD")

if PASSWORD is None:
    raise EnvironmentError("WOODSENSE_PASSWORD environment variable not set")

# Parameters
CUSTOMER_ID = "26caa6ff8d35ec28ce8b0be9"

# 1) Get access token and user
response = requests.post(
    "https://dev.woodsense.dk/api/v1/login",
    data={"username": EMAIL, "password": PASSWORD},
)
assert (
    response.status_code == 200
), f"Invalid http code received: {response.status_code}"
auth_response = response.json()
access_token = auth_response["access_token"]
user = auth_response["user"]
user_id = user["id"]
auth_headers = {"Authorization": f"Bearer {access_token}"}

# 2) Get sensors for customer
response = requests.get(
    f"https://dev.woodsense.dk/api/v1/customers/{CUSTOMER_ID}/sensors",
    headers=auth_headers,
)
assert (
    response.status_code == 200
), f"Invalid http code received: {response.status_code}"
sensors = response.json()
print(f"Found {len(sensors)} sensors")
for sensor in sensors:
    print(f"Found sensor {sensor['name']} (ID: {sensor['id']})")
