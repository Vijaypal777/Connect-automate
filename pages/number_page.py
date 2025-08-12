from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NumberPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_dialer(self):
        dialpad_icon = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@src,'dialpad-circle.svg')]"))
        )
        dialpad_icon.click()

    def select_virtual_number(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select Calling Number']"))
        ).click()

        radio_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio']"))
        )
        self.driver.execute_script("arguments[0].click();", radio_btn)

    def enter_phone_number(self, number):
        phone_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type a number or name']"))
        )
        phone_input.clear()
        phone_input.send_keys(number)

        # Trigger blur event
        self.driver.find_element(By.TAG_NAME, "body").click()
        time.sleep(1)

    # def make_call(self):
    #     call_btn_parent = self.wait.until(
    #         EC.element_to_be_clickable((By.XPATH, "//svg[contains(@class,'lucide-phone-call')]/ancestor::button"))
    #     )
    #     self.driver.execute_script("arguments[0].click();", call_btn_parent)
