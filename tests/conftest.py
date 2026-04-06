import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def set_up_browser():
    options = Options()
    options.headless = False
    driver = Chrome(
        options=options
    )
    driver.implicitly_wait(15)
    yield driver
    driver.quit()
