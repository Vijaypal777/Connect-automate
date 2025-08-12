from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InboxPage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    INBOX_BTN = (By.XPATH, "//a[@href='/inbox']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Enter your message']")
    SEND_BTN = (By.XPATH, "//svg[contains(@class, 'lucide-text-search')]")
    VIRTUAL_NUMBER_RADIO_TEMPLATE = (By.XPATH, "//input[@name='virtual-phone-number' and @value='+18884026178']")
    SEND_BTN_FLEX = (By.XPATH, "//div[contains(@class,'flex justify-around')]//button[normalize-space(text())='Send']")

    def open_inbox(self):
        print("Waiting for Inbox button and clicking...")
        self.wait.until(EC.element_to_be_clickable(self.INBOX_BTN)).click()
        print("Inbox opened.")

    def type_message(self, message):
        print("Waiting for message input...")
        input_element = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_INPUT))
        input_element.clear()
        input_element.send_keys(message)
        print(f"Typed message: {message}")


    def click_to_select_virtual_number(self):
        print("Waiting for virtual number selection and clicking...")
        virtual_number_selector = self.wait.until(EC.element_to_be_clickable(self.SEND_BTN))
        virtual_number_selector.click()
        print("Virtual number selected.")

    def click_radio_button(self):
        print("Waiting for virtual number radio button and clicking...")
        virtual_number_radio = self.wait.until(EC.element_to_be_clickable(self.VIRTUAL_NUMBER_RADIO_TEMPLATE))
        virtual_number_radio.click()
        print("Virtual number radio button clicked.")

    def click_send(self):
        print("Waiting for Send button and clicking...")
        send_button = self.wait.until(EC.element_to_be_clickable(self.SEND_BTN))
        send_button.click()
        print("Send button clicked.")



