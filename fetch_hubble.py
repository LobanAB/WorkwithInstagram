import requests
from pathlib import Path


def make_dir(target_path):
    Path(target_path).mkdir(parents=True, exist_ok=True)


def save_file(image, target_path, image_id=''):
    make_dir(target_path)
    image_name = image.split("/")[-1]
    filename = target_path + "/" + str(image_id) + image_name
    response = requests.get(image, verify=False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_hubble_images(image_id):
    api_url = "http://hubblesite.org/api/v3/image/%s" % image_id
    response = requests.get(api_url)
    response.raise_for_status()
    save_file("http:" + response.json()["image_files"][1]["file_url"], "images", image_id)


def fetch_hubble_collection(collection_name):
    api_url = "http://hubblesite.org/api/v3/images/%s?page=all" % collection_name
    response = requests.get(api_url)
    response.raise_for_status()
    for image in response.json():
        print("downloading... image id: {}".format(image["id"]))
        fetch_hubble_images(image["id"])


def main():
    fetch_hubble_collection("wallpaper")


if __name__ == '__main__':
    main()
