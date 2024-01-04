import logging
import os
import shutil
import tempfile
from argparse import ArgumentParser
from pathlib import Path

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def main():
    args = ArgumentParser()
    args.add_argument("zipfile", help="Path to unclean python zipped project")
    args = args.parse_args()
    clean_arch(args.zipfile)


def clean_arch(file):
    with tempfile.TemporaryDirectory() as temp_dir:
        extract_file(file, temp_dir)
        deleted_list = track_file(temp_dir, "__init__.py")
        log_to_file(os.path.join(temp_dir, 'cleaned.txt'), deleted_list)
        zip_folder(f"{Path(file).stem}_new", temp_dir)


def extract_file(file, where):
    try:
        shutil.unpack_archive(file, where)
    except shutil.ReadError:
        logger.error("error extracting file")


def track_file(path, file):
    deleted_list = []
    for dirpath, dirnames, files in os.walk(path, topdown=False):
        if file not in files and dirpath != path:
            relative_path = os.path.relpath(dirpath, path)
            deleted_list.append(relative_path)
            delete_dir(dirpath)
    return deleted_list


def log_to_file(filename, dir_list):
    with open(filename, 'w') as file:
        for path in sorted(dir_list):
            file.write(path)
            file.write("\n")


def delete_dir(folder):
    try:
        logger.info(f"deleting folder {folder}")
        shutil.rmtree(folder)
    except OSError as e:
        logger.error(f'Error: {folder} : {e.strerror}')


def zip_folder(zipfile, data):
    shutil.make_archive(zipfile, 'zip', data)


if __name__ == "__main__":
    main()
