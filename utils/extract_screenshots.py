from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os 
import argparse
from tqdm import tqdm

WAIT_SCREENSHOT = 0
CLUSTER = False
COLAB = False

def get_screenshot(html_file_path):
    """ Get Screenshot of website URL passed as argument, and save it """

    print("\nGenerating the screenshot ...")
    # Set webdriver options
    options = webdriver.ChromeOptions()
    options.headless = True
    if CLUSTER:
        options.binary_location = "./chrome/chrome"
    if COLAB or CLUSTER:
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    # Set window size
    options.add_argument("--window-size=1280,1024")

    # Start web browser
    if COLAB:
        driver = webdriver.Chrome('chromedriver', options=options)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)

    # Launch URL
    driver.get("file://" + os.path.abspath(html_file_path))

    # Wait some time to allow popups to show
    driver.implicitly_wait(WAIT_SCREENSHOT)

    # Obtain browser height and width
    w = driver.execute_script('return document.body.parentNode.scrollWidth')
    h = driver.execute_script('return document.body.parentNode.scrollHeight')

    # Set to new window size
    driver.set_window_size(w, h)

    # Obtain screenshot of page within body tag
    driver.find_element(By.TAG_NAME, "body").screenshot(html_file_path.replace(".html", ".png"))

    # Close web driver
    driver.close()
    print("Screenshot obtained!\n")

def extract_screenshots(folder):
    html_files = [file for file in os.listdir(folder) if file.endswith('_processed.html')] 

    for html_file in tqdm(html_files):
        get_screenshot(folder + html_file)

if __name__ == "__main__":
    folder = "results/"

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