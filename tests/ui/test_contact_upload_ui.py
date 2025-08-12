import time
import pytest
from utils.driver_setup import create_driver
from utils.config import BASE_URL, USERNAME, PASSWORD, CONTACT_LIST_NAME, FILE_PATH, CALL_NUMBER
from pages.login_page import LoginPage
from pages.contact_page import ContactPage
from pages.number_page import NumberPage

@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_contact_upload_and_call(driver):
    login_page = LoginPage(driver, BASE_URL)
    contact_page = ContactPage(driver)
    number_page = NumberPage(driver)

    login_page.load()
    login_page.login(USERNAME, PASSWORD)

    contact_page.navigate()
    contact_page.add_new_contact_list(CONTACT_LIST_NAME)
    contact_page.upload_file(FILE_PATH)

    number_page.open_dialer()
    number_page.select_virtual_number()
    number_page.enter_phone_number(CALL_NUMBER)
    # number_page.make_call()

    print("✅ Test completed successfully.")
    time.sleep(3)
