import config
import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By

# Lade Cookies einmal manuell in cookies.pkl

def upload_video(video_path, caption):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tiktok.com/upload")
    # Lade Cookies
    import pickle
    for cookie in pickle.load(open(config.TIKTOK_COOKIES_PATH, 'rb')):
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(random.uniform(5,8))
    driver.find_element(By.CSS_SELECTOR, "input[type=file]").send_keys(video_path)
    cap = driver.find_element(By.TAG_NAME, "textarea")
    cap.send_keys(caption)
    driver.find_element(By.XPATH, "//button[text()='Posten']").click()
    print("Video gepostet.")

if __name__ == '__main__':
    upload_video("./output/generated.mp4", "Deine Beschreibung #Trend")
