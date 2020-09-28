import os
from dotenv import load_dotenv
from PIL import Image
from instabot import Bot
import time
import utils


def get_resize_image(path_to_image):
    img_name = (path_to_image.split("/")[-1]).split(".")[0]
    image = Image.open(path_to_image)
    image.thumbnail((1080, 1080))
    utils.make_dir("images/thumbnail")
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
    timeout_in_seconds = 60
    bot = Bot()
    bot.login(username=username, password=password, use_cookie=True)
    for image in images_for_posting:
        bot.upload_photo("images/thumbnail/" + image, caption=image)
        time.sleep(timeout_in_seconds)


if __name__ == '__main__':
    main()
