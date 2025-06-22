from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re

# Setup Chrome options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

# Start browser
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
time.sleep(2)

# Search
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Laptop Shop near Mirpur")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Click "আরও জায়গা"
try:
    more_places = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="আরও জায়গা"]'))
    )
    more_places.click()
    print("✓ Clicked on 'আরও জায়গা'")
except Exception as e:
    print("✗ Couldn't find the button:", e)

# Container to store unique phone numbers
collected_phones = set()

# Function: Scroll and extract phones
def scroll_and_collect():
    scrollable_panel = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'center_col'))
    )
    
    for _ in range(10):
        driver.execute_script("arguments[0].scrollTop += 300;", scrollable_panel)
        time.sleep(1)

        # Collect shop cards
        shop_cards = driver.find_elements(By.XPATH, '//div[contains(@class, "rllt__details")]')
        for card in shop_cards:
            try:
                divs = card.find_elements(By.XPATH, './/div')
                for div in divs:
                    text = div.text
                    match = re.search(r'01[3-9]\d{8}', text)
                    if match:
                        phone = match.group()
                        if phone not in collected_phones:
                            collected_phones.add(phone)
                            print("✓ Found phone:", phone)
            except Exception:
                continue

# Scroll once initially
scroll_and_collect()

# Try next pages and keep collecting
while True:
    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "pnnext"))
        )
        next_button.click()
        print("✓ Clicked Next page")
        time.sleep(3)
        scroll_and_collect()
    except Exception as e:
        print("✗ No more pages or error:", e)
        break

# Save phones to file
with open("phones.txt", "w") as f:
    for phone in collected_phones:
        f.write(phone + "\n")

input("Check manually and press Enter to exit...")
driver.quit()
