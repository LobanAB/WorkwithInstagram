import os
from dotenv import load_dotenv
from pathlib import Path
from PIL import Image
from instabot import Bot  # noqa: E402
import time


def make_dir(target_path):
    Path(target_path).mkdir(parents=True, exist_ok=True)


def get_resize_image(img):
    img_name = (img.split("/")[-1]).split(".")[0]
    image = Image.open(img)
    image.thumbnail((1080, 1080))
    make_dir("images/thumbnail")
    image.save("images/thumbnail/%s.jpg" % img_name, format="JPEG")


def prepare_images_for_posting(folder):
    images = os.listdir(folder)
    for image in images:
        get_resize_image(folder + "/" + image)


def main():
    load_dotenv()
    username = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    prepare_images_for_posting("images/full_size")
    images_for_posting = os.listdir("images/thumbnail")
    timeout = 60  # pics will be posted every 1 min
    bot = Bot()
    bot.login(username=username, password=password, use_cookie=True)
    for image in images_for_posting:
        bot.upload_photo("images/thumbnail/" + image, caption=image)
        time.sleep(timeout)


if __name__ == '__main__':
    main()
