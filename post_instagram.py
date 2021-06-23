import os
from dotenv import load_dotenv
from PIL import Image
from instabot import Bot
import time
import utils
from pathlib import Path


def get_resized_image(path_to_image: Path):
    img_name = path_to_image.stem
    image = Image.open(path_to_image)
    image.thumbnail((1080, 1080))
    utils.make_dir(Path.cwd() / 'images' / 'thumbnail')
    if image.mode != "RGB":
        image = image.convert("RGB")
    image.save(
        Path.cwd() / 'images' / 'thumbnail' / (img_name + '.jpg'),
        format="JPEG"
    )


def prepare_images_for_posting(directory):
    images_names = os.listdir(directory)
    for image_name in images_names:
        get_resized_image(directory.joinpath(image_name))


def main():
    load_dotenv()
    username = os.getenv("INSTAGRAM_LOGIN")
    password = os.getenv("INSTAGRAM_PASSWORD")
    prepare_images_for_posting(Path.cwd() / 'images' / 'full_size')
    images_for_posting = os.listdir(Path.cwd() / 'images' / 'thumbnail')
    timeout_in_seconds = 60
    bot = Bot()
    bot.login(username=username, password=password, use_cookie=True)
    for image in images_for_posting:
        bot.upload_photo(
            Path.cwd() / 'images' / ('thumbnail' + image),
            caption=image
        )
        time.sleep(timeout_in_seconds)


if __name__ == '__main__':
    main()
