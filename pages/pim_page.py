from pages.base_page import BasePage

class PIMPage(BasePage):
    PIM_MENU = "text=PIM"
    ADD_EMP = "text=Add Employee"
    FIRST = "input[name='firstName']"
    LAST = "input[name='lastName']"
    SAVE = "button[type='submit']"

    def add_employee(self, fname, lname):
        self.click(self.PIM_MENU)
        self.click(self.ADD_EMP)
        self.fill(self.FIRST, fname)
        self.fill(self.LAST, lname)
        self.click(self.SAVE)