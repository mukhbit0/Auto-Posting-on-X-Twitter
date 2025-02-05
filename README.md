# Auto Posting on Twitter/X

<p align="center">
  <img src="logo.png" alt="Twitter Logo" style="border-radius: 50%; width: 140px; height: 140px;">
</p>

This script automates the process of posting images to Twitter/X. I created this for my Twitter account.

## Features

- Automatically uploads images to Twitter/X
- Adds titles and hashtags to tweets
- Uses a persistent Chrome session to avoid repeated logins
- Skips already processed images to avoid duplicates

## Requirements

- Python 3.6+
- `undetected-chromedriver`
- `selenium`

## Installation

1. Clone the repository or download the script files.
2. Navigate to the project directory.
3. Install the required packages using the following command:

   ```sh
   pip install -r requirements.txt
   ```

## Configuration

### Required

- **YEAR_FOLDER**: Path to the folder containing your images.
- **USER_DATA_DIR**: Path to your Chrome user data directory.

### Optional

- **HASHTAGS**: Hashtags to be added to the tweets.
- **MAX_TWEETS_PER_RUN**: Maximum number of tweets to process in one run (default is 10).
- **TEXT_FILE_NAME**: Name of the text file containing additional details for the tweets (default is `details.txt`).

## Usage

1. Ensure that the required configurations are set in the script.
2. Run the script using the following command:

   ```sh
   python x.py
   ```

3. The script will open a Chrome browser and navigate to Twitter/X.
4. If this is the first time running the script, you will be prompted to log in to Twitter/X. After logging in, press Enter to continue.
5. The script will process up to the specified number of images from the configured folder, uploading them to Twitter/X and adding the necessary details.
6. After processing the images, you will be prompted to publish the tweets manually. Press Enter to continue.
7. The script will save the processed images to the log file and exit.

## Contributing

If you would like to contribute to this project, please email [mukhbit000@gmail.com](mailto:mukhbit000@gmail.com).

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## ☕ Support My Work  
**Love this project?** Help me keep building automation tools!  
---[Buy Me a Coffee](https://buymeacoffee.com/mukhbit) → Every sip fuels more code! 🚀  

---

## ☕ Support My Work  
<div align="center">
  <a href="https://buymeacoffee.com/mukhbit">
    <img src="https://miro.medium.com/v2/resize:fit:1090/0*lHgOW3tB_MfDAlBf.png" alt="Buy Me A Coffee" style="width: 200px;">
  </a>
</div>