import os
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
CONTACT_LIST_NAME = "Test Contact"
FILE_PATH = r"D:\AtoZ\Connect_automate\fake_contacts.xlsx"
CALL_NUMBER = "+917206907047"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Login
    driver.get(f"{BASE_URL}/sign-in")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
    ).send_keys(USERNAME)

    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()

    WebDriverWait(driver, 15).until(
        EC.url_to_be(f"{BASE_URL}/dashboard")
    )
    print("✅ Login successful.")

    # Navigate to contacts
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/contacts' and span[normalize-space()='Contacts']]"))
    ).click()

    # Add new contact list
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(.),'Add New Contact')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "name"))
    ).send_keys(CONTACT_LIST_NAME)

    driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    # Upload file
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"❌ File not found: {FILE_PATH}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "selectListFile"))
    )

    hidden_input = driver.find_element(By.XPATH, "//label[@id='selectListFile']/input[@type='file']")
    driver.execute_script(
        "arguments[0].removeAttribute('hidden'); arguments[0].style.display='block';",
        hidden_input
    )

    hidden_input.send_keys(FILE_PATH)
    print(f"📂 File uploaded: {FILE_PATH}")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
    ).click()

    # Go to dialer
    dialpad_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[contains(@src,'dialpad-circle.svg')]"))
    )
    dialpad_icon.click()
    print("📞 Dialer opened.")

    # Select virtual number
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select Calling Number']"))
    ).click()

    radio_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='radio']"))
    )
    driver.execute_script("arguments[0].click();", radio_btn)
    print("✅ Virtual number selected.")

    # Enter phone number
    phone_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type a number or name']"))
    )
    phone_input.clear()
    phone_input.send_keys(CALL_NUMBER)
    print(f"📲 Entered number: {CALL_NUMBER}")

    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(1)

    # Make call
    call_btn_parent = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//svg[contains(@class,'lucide-phone-call')]/ancestor::button"))
    )
    driver.execute_script("arguments[0].click();", call_btn_parent)
    print("📞 Call initiated.")

    print("✅ Process completed successfully.")
    time.sleep(3)

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
