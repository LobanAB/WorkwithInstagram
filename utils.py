from pathlib import Path


def make_dir(target_path):
    Path(target_path).mkdir(parents=True, exist_ok=True)