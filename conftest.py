import pytest
from utils.driver_setup import create_driver

@pytest.fixture(scope="session")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()
