from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from utils.config import *

def test_e2e_flow(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    dash = DashboardPage(page)
    assert dash.is_loaded()

    pim = PIMPage(page)
    pim.add_employee("Auto", "User")

    dash.logout()