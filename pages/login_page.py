from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    def load(self):
        self.driver.get(f"{self.base_url}/sign-in")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
        self.wait.until(EC.url_to_be(f"{self.base_url}/dashboard"))
