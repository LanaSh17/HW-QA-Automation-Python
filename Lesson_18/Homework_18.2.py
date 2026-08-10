import requests
from urllib.parse import urlparse


BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "image.jpg"


# POST - upload image
with open(IMAGE_PATH, "rb") as image:
    files = {
        "image": image
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

print("POST /upload")
print("Status code:", response.status_code)
print("Response:", response.json())


image_url = response.json()["image_url"]
print("Image URL:", image_url)


filename = urlparse(image_url).path.split("/")[-1]
print("Filename:", filename)


# GET - get image URL
response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers={"Content-Type": "text"}
)

print("GET /image/")
print("Status code:", response.status_code)
print("Response:", response.json())


# DELETE - delete image
response = requests.delete(
    f"{BASE_URL}/delete/{filename}"
)

print("DELETE /delete/")
print("Status code:", response.status_code)
print("Response:", response.json())