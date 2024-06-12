import sys
import os
import re
import requests
import bs4
from tqdm import tqdm

def download_video(url, file_name) -> None:
    download_dir = "D:\\Downloaded Videos"
    os.makedirs(download_dir, exist_ok=True)
    download_path = os.path.join(download_dir, file_name)
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit="B", unit_scale=True, desc=f"Downloading {file_name}")

    with open(download_path, "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()
    print(f"Video downloaded to {download_path}")

def download_twitter_video(url, custom_name=None):
    print("Fetching video information...")
    api_url = f"https://twitsave.com/info?url={url}"

    response = requests.get(api_url)
    data = bs4.BeautifulSoup(response.text, "html.parser")
    download_button = data.find_all("div", class_="origin-top-right")[0]
    quality_buttons = download_button.find_all("a")
    highest_quality_url = quality_buttons[0].get("href")

    print("Extracting video details...")
    file_name = data.find_all("div", class_="leading-tight")[0].find_all("p", class_="m-2")[0].text
    file_name = re.sub(r"[^a-zA-Z0-9çÇğĞıİöÖşŞüÜ]+", ' ', file_name).strip()

    if custom_name:
        file_name = re.sub(r"[^a-zA-Z0-9çÇğĞıİöÖşŞüÜ]+", ' ', custom_name).strip()
    
    file_name += ".mp4"

    print(f"Downloading video: {file_name}")
    download_video(highest_quality_url, file_name)
    print("Download complete.")

if len(sys.argv) < 2:
    print("Usage: python twitter_downloader.py <URL>")
else:
    url = sys.argv[1]
    if url:
        custom_name = input("Enter a custom name for the video (or press Enter to use the default name): ").strip()
        if custom_name == "":
            custom_name = None
        download_twitter_video(url, custom_name)
    else:
        print("Invalid Twitter video URL.")
