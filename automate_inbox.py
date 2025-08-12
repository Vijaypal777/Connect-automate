import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://devconnectapp.teldrip.com"
USERNAME = "moaning.wolverine.pxou@letterhaven.net"
PASSWORD = "Test@1234"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # 1. LOGIN
    driver.get(f"{BASE_URL}/sign-in")
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
    ).send_keys(USERNAME)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
    WebDriverWait(driver, 20).until(EC.url_contains("/dashboard"))
    print("✅ Login successful.")

    # 2. GO TO INBOX
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/inbox']"))
    ).click()
    print("Clicked Inbox")

    # 3. TYPE MESSAGE
    message_input = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter your message']"))
    )
    message_input.clear()
    message_input.send_keys("Hello, this is a test message.")
    print("Typed message")

    # 4. FIND SEND ROW (composer) AND TARGET ONLY THAT MAGNIFIER ICON
    send_row_xpath = "//input[@placeholder='Enter your message']/following-sibling::div[contains(@class, 'flex') and contains(@class, 'justify-around')]"
    send_row = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, send_row_xpath))
    )
    # The magnifier icon is the last div in this send_row container
    icon_xpath = ".//div[contains(@class, 'cursor-pointer') and .//svg[contains(@class, 'lucide-text-search')]]"
    search_icons = send_row.find_elements(By.XPATH, icon_xpath)
    found = False
    for icon in search_icons:
        if icon.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", icon)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", icon)
            print("Clicked search/magnifier icon in send row")
            found = True
            break
    if not found:
        raise Exception("❌ Could not find visible search icon in send row!")

    # 5. WAIT FOR RADIO TO APPEAR AND CLICK
    radio_xpath = "//input[@type='radio' and @name='virtual-phone-number' and @value='+18884026178']"
    radio_elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, radio_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_elem)
    radio_elem.click()
    print("Selected virtual number radio")

    # 6. CLICK SEND BUTTON (always the first button in send row)
    send_btn = send_row.find_element(By.XPATH, ".//button[normalize-space()='Send']")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//button[normalize-space()='Send']")))
    send_btn.click()
    print("Clicked Send")

    time.sleep(2)  # Let UI update before close

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
    