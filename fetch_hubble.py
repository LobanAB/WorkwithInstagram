import requests
import utils
from pathlib import Path


def fetch_hubble_image(image_id_list: list, images_dir='images', images_subdir='full_size'):
    for image_id in image_id_list:
        api_url = f"http://hubblesite.org/api/v3/image/{image_id}"
        response = requests.get(api_url)
        response.raise_for_status()
        utils.save_image(
            "http:" + response.json()["image_files"][0]["file_url"],
            Path.cwd() / images_dir / images_subdir,
            image_id
        )


def fetch_hubble_collection(collection_name='news'):
    api_url = f"http://hubblesite.org/api/v3/images/{collection_name}"
    payload = {"page": 'all'}
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    return [image["id"] for image in response.json()]


def main():
    images_dir = 'images'
    images_subdir = 'full_size'
    collection_name = 'news'
    fetch_hubble_image(fetch_hubble_collection(collection_name), images_dir, images_subdir)


if __name__ == '__main__':
    main()
