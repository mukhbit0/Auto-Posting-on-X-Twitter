import os
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random

# Configuration
YEAR_FOLDER = "C:\\Users\\arslan\\Videos\\ai\\ai\\New folder\\Minimalist Poster\\Anime\\Filtered Shikimori Poster\\ByYear\\ByYear\\2025"
LOG_FILE = "processed_tweets.txt"
SESSION_LOG_FILE = "twitter_session.txt"
FAILED_LOG_FILE = "failed_tweets.txt"
DUPLICATE_LOG_FILE = "duplicate_tweets.txt"
MAX_TWEETS_PER_RUN = 10
TEXT_FILE_NAME = "details.txt"
USER_DATA_DIR = os.path.join(os.getcwd(), "TwitterProfile")
HASHTAGS = "#Anime #Manga #Art #Design #Otaku"

def human_like_delay(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))

def get_base_text(image_path):
    text_file = os.path.join(os.path.dirname(image_path), TEXT_FILE_NAME)
    if os.path.exists(text_file):
        with open(text_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "Anime Minimalist Poster Collection 🎨"

def generate_tweet_content(image_path):
    filename = os.path.basename(image_path).split('.')[0]
    clean_name = re.sub(r'[\W_]+', ' ', filename).title()
    base_text = get_base_text(image_path)
    return f"{base_text}\n{HASHTAGS}"

def create_driver():
    options = uc.ChromeOptions()
    options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return uc.Chrome(options=options)

def prepare_tweet(driver, image_path):
    try:
        # Open new tab
        driver.switch_to.new_window('tab')
        driver.get("https://x.com/compose/post")
        
        # Wait for editor
        editor = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Post text"]'))
        )
        
        # Enter text
        editor.click()
        human_like_delay()
        editor.send_keys(generate_tweet_content(image_path))
        
        # Upload image
        file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
        file_input.send_keys(image_path)
        
        # Verify upload
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="attachments"]'))
        )
        
        print(f"Successfully prepared: {os.path.basename(image_path)}")
        return True

    except Exception as e:
        print(f"Failed to prepare tweet: {str(e)}")
        save_processed_file(FAILED_LOG_FILE, os.path.basename(image_path))
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return False

def load_processed_files(log_file):
    """Load processed files with encoding handling"""
    processed = set()
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                processed = set(line.strip() for line in f)
        except UnicodeDecodeError:
            with open(log_file, "r", encoding="latin-1") as f:
                processed = set(line.strip() for line in f)
    return processed

def save_processed_file(log_file, filename):
    """Save processed file with UTF-8 encoding"""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{filename}\n")

def main():
    driver = create_driver()
    try:
        # Check login
        driver.get("https://x.com/home")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="/compose/post"]'))
            )
        except TimeoutException:
            input("Please login in the browser window and press Enter to continue...")

        # Load processed files
        processed = load_processed_files(LOG_FILE)

        # Process images
        image_files = []
        for root, _, files in os.walk(YEAR_FOLDER):
            for f in files:
                if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_files.append(os.path.join(root, f))
        
        random.shuffle(image_files)
        success_count = 0
        new_processed = []

        for img_path in image_files[:MAX_TWEETS_PER_RUN]:
            if os.path.basename(img_path) in processed:
                print(f"Skipping duplicate: {os.path.basename(img_path)}")
                save_processed_file(DUPLICATE_LOG_FILE, os.path.basename(img_path))
                continue

            if prepare_tweet(driver, img_path):
                success_count += 1
                new_processed.append(os.path.basename(img_path))
                human_like_delay(10, 15)

        input(f"\n{success_count} tweets prepared in browser tabs. Review and post manually, then press Enter to exit...")

        # Save processed files
        for filename in new_processed:
            save_processed_file(LOG_FILE, filename)

        print(f"Total tweets processed: {success_count}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()