from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from utils.config import *
import time
from utils.logger import get_logger

logger = get_logger()


def test_add_candidate(page):
    logger.info("Starting test_add_candidate")

    # Login
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    # Navigate to Recruitment
    recruit = RecruitmentPage(page)
    recruit.navigate_to_recruitment()

    # Dynamic name
    first_name = "Yashoda"
    last_name = "QA_" + str(int(time.time()))

    # Add candidate
    recruit.add_candidate(first_name, last_name)

    # Validation
    assert recruit.is_candidate_added()