from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from utils.config import *

def test_add_employee(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    pim = PIMPage(page)
    pim.add_employee("Yashoda", "QA")