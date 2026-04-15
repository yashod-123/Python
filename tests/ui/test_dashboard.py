from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import *

def test_dashboard(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    dash = DashboardPage(page)
    assert dash.is_loaded()

def test_logout(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    dash = DashboardPage(page)
    dash.logout()
    assert "login" in page.url