import requests
import utils
from pathlib import Path


def fetch_spacex_last_launch():
    api_url = "https://api.spacexdata.com/v3/launches/74"
    response = requests.get(api_url)
    response.raise_for_status()
    images = response.json()["links"]["flickr_images"]
    for image in images:
        utils.save_image(image, Path.cwd() / 'images' / 'full_size')


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
