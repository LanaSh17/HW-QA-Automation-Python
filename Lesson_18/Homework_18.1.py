import requests

BASE_URL = "https://images-api.nasa.gov"

# 1. Пошук зображень, пов'язаних з ровером Curiosity на Марсі
search_url = f"{BASE_URL}/search"

search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()

search_data = search_response.json()

items = search_data.get("collection", {}).get("items", [])

# 2. nasa_id для знайдених елементів
nasa_ids = []

for item in items:
    nasa_id = item.get("data", [{}])[0].get("nasa_id")

    if nasa_id:
        nasa_ids.append(nasa_id)

print(f"nasa_id: {nasa_ids}")

# Беремо перші два nasa_id
selected_ids = nasa_ids[:2]

if len(selected_ids) < 2:
    raise Exception("Не знайдено достатньо зображень.")


# 3. Отримуємо список файлів для кожного nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

jpg_urls = []

for nasa_id in selected_ids:

    asset_url = asset_url_template.format(nasa_id=nasa_id)

    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()

    asset_data = asset_response.json()

    asset_items = asset_data.get("collection", {}).get("items", [])

# 4. Знаходимо JPG-файл
    jpg_url = None

    for asset_item in asset_items:
        href = asset_item.get("href", "")

        if href.lower().endswith(".jpg"):
            jpg_url = href
            break

    if jpg_url:
        jpg_urls.append(jpg_url)
        print(f"{nasa_id}: {jpg_url}")
    else:
        print(f"Для {nasa_id} JPG не знайдено.")


# 5. Скачуємо два зображення
file_names = [
    "mars_photo1.jpg",
    "mars_photo2.jpg"
]

for jpg_url, file_name in zip(jpg_urls[:2], file_names):

    image_response = requests.get(jpg_url)
    image_response.raise_for_status()

    with open(file_name, "wb") as file:
        file.write(image_response.content)

    print(f"Зображення збережено: {file_name}")
