class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):

        self.page.goto(url, timeout=60000, wait_until="domcontentloaded")

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def wait(self, locator):
        self.page.locator(locator).wait_for()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()