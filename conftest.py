import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        # ✅ Screenshot on failure
        if request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{request.node.name}.png")

        browser.close()


# Hook to get test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)