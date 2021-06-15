import requests
import utils
from pathlib import Path


def fetch_hubble_image(image_id):
    api_url = f"http://hubblesite.org/api/v3/image/{image_id}"
    response = requests.get(api_url)
    response.raise_for_status()
    utils.save_image(
        "http:" + response.json()["image_files"][0]["file_url"],
        Path.cwd() / 'images' / 'full_size',
        image_id
    )


def fetch_hubble_collection(collection_name):
    api_url = f"http://hubblesite.org/api/v3/images/{collection_name}?page=all"
    response = requests.get(api_url)
    response.raise_for_status()
    for image in response.json():
        fetch_hubble_image(image["id"])


def main():
    fetch_hubble_collection("news")


if __name__ == '__main__':
    main()
