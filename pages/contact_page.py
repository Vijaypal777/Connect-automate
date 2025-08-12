from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/contacts' and span[normalize-space()='Contacts']]"))
        ).click()

    def add_new_contact_list(self, contact_list_name):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(.),'Add New Contact')]"))
        ).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(contact_list_name)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def upload_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        self.wait.until(EC.presence_of_element_located((By.ID, "selectListFile")))
        hidden_input = self.driver.find_element(By.XPATH, "//label[@id='selectListFile']/input[@type='file']")

        # Make hidden file input visible and send file path
        self.driver.execute_script(
            "arguments[0].removeAttribute('hidden'); arguments[0].style.display='block';", hidden_input
        )
        hidden_input.send_keys(file_path)

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
