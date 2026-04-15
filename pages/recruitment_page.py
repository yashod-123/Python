import time

from pages.base_page import BasePage


class RecruitmentPage(BasePage):
    RECRUITMENT_MENU = "text=Recruitment"
    ADD_BTN = "text=Add"

    FIRST_NAME = "input[name='firstName']"
    LAST_NAME = "input[name='lastName']"
    EMAIL = "//input[@placeholder='Type here'][1]"

    SAVE_BTN = "button[type='submit']"
    SUCCESS_MSG = "text=Success"
    CONTACT = "(//input[@placeholder='Type here'])[3]"

    def navigate_to_recruitment(self):
        self.click(self.RECRUITMENT_MENU)

    def add_candidate(self, first, last):
        self.click(self.ADD_BTN)

        self.page.wait_for_selector(self.FIRST_NAME)

        # Names
        self.page.locator(self.FIRST_NAME).fill(first)
        self.page.locator(self.LAST_NAME).fill(last)

        # Email
        email = f"yashoda{int(time.time())}@gmail.com"
        self.page.locator("input[placeholder='Type here']").nth(0).fill(email)

        # Contact Number
        self.page.locator("input[placeholder='Type here']").nth(1).fill("9876543210")

        # ✅ Select Vacancy (IMPORTANT)
        self.page.locator("div.oxd-select-text").click()
        self.page.locator("span:has-text('Software Engineer')").click()

        # Save
        self.page.locator(self.SAVE_BTN).click()

    def is_candidate_added(self):
        try:
            self.page.locator("div.oxd-toast-content").wait_for(timeout=5000)
            return True
        except:
            return "viewCandidate" in self.page.url