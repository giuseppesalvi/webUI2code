from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import argparse
from tqdm import tqdm

from webgenerator.ScreenShutter import ScreenShutter

CHROME_DRIVER_PATH = './chromedriver/mac_arm-116.0.5845.96/chromedriver-mac-arm64/chromedriver'


def extract_screenshots(folder):
    # Generate multiple webpages and screenshots
    screen_shutter = ScreenShutter(full_screenshot=False, show_progress=False, input_path=folder,
                                   output_path="results/", assets_path="utils/webgenerator/Assets/", driver_path=CHROME_DRIVER_PATH)
    screen_shutter.capture_and_save()


if __name__ == "__main__":
    folder = "results/demo"

    # Initialize args parser
    parser = argparse.ArgumentParser(description="Extract screenshots from html files inside a local folder",
                                     usage="python3 extract_screenshots.py --folder {folder}")
    parser.add_argument("--folder",
                        help="Folder with html files to extract screenshots from")

    # Read args
    args = parser.parse_args()

    if args.folder:
        folder = args.folder
        if not folder.endswith("/"):
            folder = folder + "/"

    extract_screenshots(folder)
