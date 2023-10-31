import os

import requests

# Credentials
EMAIL = "lasse@woodsense.com"
PASSWORD = os.getenv("WOODSENSE_PASSWORD")

if PASSWORD is None:
    raise EnvironmentError("WOODSENSE_PASSWORD environment variable not set")

# Parameters
SENSOR_ID = "0fc0f474c4637a8c5a6257a6"
FROM_TIMESTAMP_ISO = "2023-10-01T00:00:00.000Z"
TO_TIMESTAMP_ISO = "2023-10-08T00:00:00.000Z"


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

# 2) Load transmissions for sensor
response = requests.get(
    f"https://dev.woodsense.dk/api/v1/sensors/{SENSOR_ID}/transmissions",
    params={
        "from_timestamp": FROM_TIMESTAMP_ISO,
        "to_timestamp": TO_TIMESTAMP_ISO,
    },
    headers=auth_headers,
)
assert (
    response.status_code == 200
), f"Invalid http code received: {response.status_code}"
transmissions = response.json()
print(*transmissions, sep="\n")
