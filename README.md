# Streamlit Web Scraping Tool with Selenium, Ollama, and Bright Data

A Python-based web scraping app featuring:

- **Streamlit:** An easy-to-use framework to build interactive web apps.
- **Selenium:** A powerful tool for automating and controlling web browsers to scrape data.
- **Ollama:** Local large language model (LLM) integration to process and analyze scraped data.
- **Bright Data:** A proxy service that helps bypass CAPTCHAs and access websites reliably during scraping.

---

## Features

- Interactive UI built with Streamlit.
- Automated browser navigation and scraping using Selenium.
- Local LLM support via Ollama for data processing.
- CAPTCHA bypass and IP rotation with Bright Data proxies.

---

## Prerequisites

- Python 3.7+
- Google Chrome installed
- ChromeDriver matching your Chrome version (download link in `instructions.txt`)
- Ollama installed and running locally
- Bright Data proxy account and setup

---

## Installation

1. Clone this repository:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>

    Install dependencies listed in instructions.txt:

pip install -r instructions.txt

Install ChromeDriver:

Download the correct version from the link in instructions.txt. Make sure it matches your Chrome version and add it to your system PATH.

Set up Ollama:

    Install Ollama from Ollama docs.

    Pull the required LLM model:

ollama pull name_of_model

Run the model locally:

        ollama run name_of_model

    Configure Bright Data:

    Ensure your Bright Data proxy credentials and configuration are set correctly in the app or environment variables.

Running the Application

Start the Streamlit web app:

streamlit run app.py

Access the app in your browser at: http://localhost:8501
Notes

    Make sure ChromeDriver version matches your installed Chrome browser.

    Ollama must be running before launching the app for LLM features.

    Bright Data proxies require valid credentials to bypass CAPTCHA and avoid IP bans.

License

This project is licensed under the MIT License.
Contact

Feel free to open an issue or contact the maintainer for support.
