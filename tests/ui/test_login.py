import os

os.system("python setup.py")


from pages.login_page import LoginPage
from utilities.utils import get_login_credentials


class TestLogin:

    def test_login_successful(self, driver):
        login_page = LoginPage(driver)
        username, password = get_login_credentials()
        login_page.login(username, password)
        assert driver.title == "Trello"
