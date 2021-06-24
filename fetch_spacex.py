import requests
import utils
from pathlib import Path


def fetch_spacex_last_launch(images_dir='images', images_subdir='full_size'):
    api_url = "https://api.spacexdata.com/v3/launches/74"
    response = requests.get(api_url)
    response.raise_for_status()
    images = response.json()["links"]["flickr_images"]
    utils.make_dir(Path.cwd() / images_dir / images_subdir)
    for image in images:
        utils.save_image(image, Path.cwd() / images_dir / images_subdir)


def main():
    images_dir = 'images'
    images_subdir = 'full_size'
    fetch_spacex_last_launch(images_dir, images_subdir)


if __name__ == '__main__':
    main()
