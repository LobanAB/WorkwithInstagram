import requests
from pathlib import Path


def make_dir(target_path: Path):
    Path(target_path).mkdir(parents=True, exist_ok=True)


def save_image(image_url: str, target_path: Path, image_id=''):
    make_dir(target_path)
    image_name = image_url.split("/")[-1]
    filename = target_path.joinpath(f'{image_id}{image_name}')
    response = requests.get(image_url, verify=False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
