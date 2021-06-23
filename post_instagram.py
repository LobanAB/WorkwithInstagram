import os
from dotenv import load_dotenv
from PIL import Image
from instabot import Bot
import time
import utils
from pathlib import Path


def save_resized_image(
        path_to_image_list: list,
        images_dir='images',
        images_thumbnail_subdir='thumbnail',
        ig_image_height=1080,
        ig_image_width=1080):
    for path_to_image in path_to_image_list:
        img_name = path_to_image.stem
        image = Image.open(path_to_image)
        image.thumbnail((ig_image_width, ig_image_height))
        utils.make_dir(Path.cwd() / images_dir / images_thumbnail_subdir)
        if image.mode != "RGB":
            image = image.convert("RGB")
        image.save(
            Path.cwd() / images_dir / images_thumbnail_subdir / (img_name + '.jpg'),
            format="JPEG"
        )


def get_images_for_posting_list(directory):
    images_names = os.listdir(directory)
    return [directory.joinpath(image_name) for image_name in images_names]


def post_to_instagram(
        username,
        password,
        images_dir,
        images_thumbnail_subdir,
        post_timeout_in_seconds
):
    images_for_posting = os.listdir(Path.cwd() / images_dir / images_thumbnail_subdir)
    bot = Bot()
    bot.login(username=username, password=password, use_cookie=True)
    for image in images_for_posting:
        bot.upload_photo(
            Path.cwd() / images_dir / (images_thumbnail_subdir + image),
            caption=image
        )
        time.sleep(post_timeout_in_seconds)


def main():
    load_dotenv()
    username = os.getenv("INSTAGRAM_LOGIN")
    password = os.getenv("INSTAGRAM_PASSWORD")
    images_dir = 'images'
    images_subdir = 'full_size'
    images_thumbnail_subdir = 'thumbnail'
    post_timeout_in_seconds = 60
    ig_image_height = 1080
    ig_image_width = 1080
    path_to_image_list = get_images_for_posting_list(Path.cwd() / images_dir / images_subdir)
    save_resized_image(path_to_image_list, images_dir, images_thumbnail_subdir, ig_image_height, ig_image_width)
    post_to_instagram(username, password, images_dir, images_thumbnail_subdir, post_timeout_in_seconds)


if __name__ == '__main__':
    main()
