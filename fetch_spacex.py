import requests
from pathlib import Path


def make_dir(target_path):
    Path(target_path).mkdir(parents=True, exist_ok=True)


def save_file(image, target_path):
    make_dir(target_path)
    image_name = image.split("/")[-1]
    filename = target_path + "/" + image_name
    response = requests.get(image, verify=False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    api_url = "https://api.spacexdata.com/v3/launches/74"
    response = requests.get(api_url)
    response.raise_for_status()
    images = response.json()["links"]["flickr_images"]
    for image in images:
        save_file(image, "images/full_size")


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
