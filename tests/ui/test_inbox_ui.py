import time
import pytest
from pages.inbox_page import InboxPage
from utils.driver_setup import create_driver
from utils.config import BASE_URL, USERNAME, PASSWORD



def test_send_message_flow(driver):
    driver.get(f"{BASE_URL}/sign-in")

    from pages.login_page import LoginPage
    login_page = LoginPage(driver, BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inbox_page = InboxPage(driver)
    
    inbox_page.open_inbox()
    inbox_page.type_message("Hello, this is a test message.")
    inbox_page.click_to_select_virtual_number()
    inbox_page.click_radio_button()
    inbox_page.click_send()

    