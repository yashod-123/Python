from pages.login_page import LoginPage
from utils.config import *

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)
    # assert "dashboard" in page.url
    page.wait_for_url("**/dashboard/**", timeout=10000)
    assert "dashboard" in page.url

def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login("wrong", "wrong")
    assert "Invalid" in login.get_error()