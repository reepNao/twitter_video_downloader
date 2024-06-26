# Twitter Video Downloader

This Python script allows you to download videos from Twitter. It retrieves the highest quality video available for a given Twitter video URL and saves it to your local machine.

## Requirements

- Python 3
- requests
- tqdm
- beautifulsoup4

## Usage

1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/reepNao/twitter_video_downloader.git
```

2. Navigate to the directory where the script is located.

3. You can install the required packages by running:

```bash
pip install -r requirements.txt
```

4. Run the script using the following command:

```bash
python twitter_mp4_downloader.py <URL>
```

Replace `<URL>` with the URL of the Twitter video you want to download.

4. If you want to specify a custom name for the downloaded video, you will be prompted to enter it. Otherwise, the default name will be used.


## Notes

- This script relies on the twitsave.com service to fetch video information from Twitter. If the service is down or changes its structure, the script may not work as expected.
