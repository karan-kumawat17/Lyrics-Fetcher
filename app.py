import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver with options
def setup_driver():
    service = Service('./chromedriver-win32/chromedriver-win32/chromedriver.exe')  # Adjust the path to your ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ensure headless is being added as an argument
    options.add_argument("--disable-gpu")  # This option is often recommended to run headless
    options.add_argument("--window-size=1920,1080")  # Specify the window size
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    options.add_argument("--log-level=OFF")
    options.add_argument("--disable-logging")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # This option specifically targets ChromeDriver logs.
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Perform search on AZLyrics
def perform_search(driver, search_query):
    driver.get("https://www.azlyrics.com")
    search_box = driver.find_element(By.CSS_SELECTOR, ".search input[type='text']")
    search_box.send_keys(search_query + Keys.RETURN)
    time.sleep(5)  # Adjust timing based on your testing
    return driver  # Return the driver instead of URL to continue interaction

# Navigate search results to find the first song link and click it
def navigate_search_results(driver):
    try:
        # Finding the first link within the search results to click
        results_label = driver.find_element(By.XPATH, "//b[contains(text(), 'Song results:')]")
        results_panel = results_label.find_element(By.XPATH, "./ancestor::div[@class='panel']")
        links = results_panel.find_elements(By.TAG_NAME, "a")
        if links:
            links[0].click()
            time.sleep(2)  # Wait for the lyrics page to load
            return driver  # Continue with the same driver instance
        else:
            print("No song links found in the results.")
            return None
    except Exception as e:
        print("Error navigating results:", e)
        return None

# Scrape lyrics from the AZLyrics page
def scrape_lyrics(driver):
    try:
        # Assuming that the song page is now open
        ringtone_div = driver.find_element(By.CLASS_NAME, "ringtone")
        lyrics_element = ringtone_div.find_element(By.XPATH, "./following-sibling::div")
        lyrics = lyrics_element.text
        return lyrics
    except Exception as e:
        print("Error scraping lyrics:", e)
        return None
    finally:
        driver.quit()

# Streamlit UI
st.title("Song Lyrics Fetcher")
song_name = st.text_input("Enter the name of the song:", "")
if song_name:
    if st.button("Fetch Lyrics"):
        driver = setup_driver()
        driver = perform_search(driver, song_name)
        if driver:
            driver = navigate_search_results(driver)
            if driver:
                lyrics = scrape_lyrics(driver)
                st.text_area("Lyrics:", value=lyrics, height=300)
            else:
                st.error("Could not navigate to song lyrics page.")
        else:
            st.error("Search did not return any results.")
