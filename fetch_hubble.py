import requests
import utils
from pathlib import Path


def save_file(image_url, target_path, image_id):
    utils.make_dir(target_path)
    image_name = image_url.split("/")[-1]
    filename = target_path.joinpath(str(image_id) + image_name)
    response = requests.get(image_url, verify=False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_hubble_image(image_id):
    api_url = f"http://hubblesite.org/api/v3/image/{image_id}"
    response = requests.get(api_url)
    response.raise_for_status()
    save_file("http:" + response.json()["image_files"][1]["file_url"], Path.cwd() / 'images' / 'full_size', image_id)


def fetch_hubble_collection(collection_name):
    api_url = f"http://hubblesite.org/api/v3/images/{collection_name}?page=all"
    response = requests.get(api_url)
    response.raise_for_status()
    for image in response.json():
        fetch_hubble_image(image["id"])


def main():
    fetch_hubble_collection("wallpaper")


if __name__ == '__main__':
    main()
