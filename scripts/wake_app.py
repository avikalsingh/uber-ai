import os
import sys
from playwright.sync_api import sync_playwright

APP_URL = "https://uber-ai.streamlit.app/"

def wake_streamlit():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Navigating to {APP_URL}...")
        page.goto(APP_URL, wait_until="networkidle", timeout=60000)

        # Selector matches Streamlit's "Yes, get this app back up!" button
        wake_button = page.locator('button:has-text("Yes, get this app back up!"), button:has-text("Wake")')

        if wake_button.is_visible():
            print("App is sleeping. Clicking wake button...")
            wake_button.click()
            # Wait for container reboot and initial app UI rendering
            page.wait_for_timeout(15000)
            print("Wake button triggered successfully.")
        else:
            print("App is already awake and responsive.")

        browser.close()

if __name__ == "__main__":
    try:
        wake_streamlit()
    except Exception as e:
        print(f"Error executing wake routine: {e}")
        sys.exit(1)
