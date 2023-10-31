import os

import requests

# Credentials
EMAIL = "lasse@woodsense.com"
PASSWORD = os.getenv("WOODSENSE_PASSWORD")

if PASSWORD is None:
    raise EnvironmentError("WOODSENSE_PASSWORD environment variable not set")

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

# 2) Get users customers
response = requests.get(
    f"https://dev.woodsense.dk/api/v1/users/{user_id}/customers",
    headers=auth_headers,
)
assert (
    response.status_code == 200
), f"Invalid http code received: {response.status_code}"
customers = response.json()

# 3) Get sensors for each customer
for customer in customers:
    print(f"Found customer: {customer['name']} (ID: {customer['id']})")
