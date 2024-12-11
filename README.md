# Lyrics Fetcher

## About the Project
This project is a **Lyrics Fetcher** developed to demonstrate the power of web scraping. Using this tool, you can search for any song, and it will fetch the lyrics for you.

## Prerequisites
To run this project, ensure you have the following:

1. **ChromeDriver**: Download the latest version of ChromeDriver compatible with your Chrome browser from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads). Extract the downloaded folder. The folder structure should look like this:
```
chromedriver-win32/
└── chromedriver.exe
```

2. **Python and Required Libraries**:
- Install Python (if not already installed).
- Install the required libraries:
  ```bash
  pip install streamlit selenium
  ```
  Or if you use conda:
  ```bash
  conda install -c conda-forge streamlit selenium
  ```

## How to Run the Project

1. **Set Up the Directory**
- Clone this repository to your local machine.
- Ensure the `chromedriver-win32` folder is in the same directory as the cloned repository. For example:
  ```
  hehe/
  ├── chromedriver-win32/
  │   └── chromedriver.exe
  └── Lyrics-Fetcher/
  ```

2. **Navigate to the Project Directory**
Open a terminal or command prompt and navigate to the `Lyrics-Fetcher` directory.

3. **Run the Application**
- Start the Streamlit app by running:
  ```bash
  streamlit run app.py
  ```

4. **Fetch Lyrics**
- Open the link provided by Streamlit in your browser.
- Enter the name of the song you want to search for.
- The app will scrape and display the lyrics for the song.

## Purpose
This project is purely designed to showcase web scraping using Selenium and Streamlit. Enjoy exploring the power of web scraping with this tool!
