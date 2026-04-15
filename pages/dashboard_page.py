from pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADER = "h6:has-text('Dashboard')"
    PROFILE = ".oxd-userdropdown-tab"
    LOGOUT = "text=Logout"

    def is_loaded(self):
        self.wait(self.HEADER)
        return self.is_visible(self.HEADER)

    def logout(self):
        self.click(self.PROFILE)
        self.click(self.LOGOUT)