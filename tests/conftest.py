import pytest
from playwright.sync_api import Playwright, Page

BASE_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course'
REGISTRATION_URL = f'{BASE_URL}/#/auth/registration'
STATE_PATH = 'browser-state.json'


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(REGISTRATION_URL)

    email_input = page.get_by_test_id(
        'registration-form-email-input'
    ).locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id(
        'registration-form-username-input'
    ).locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id(
        'registration-form-password-input'
    ).locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id(
        'registration-page-registration-button'
    )
    registration_button.click()

    page.get_by_test_id('dashboard-toolbar-title-text').wait_for()

    context.storage_state(path=STATE_PATH)
    browser.close()


@pytest.fixture
def chromium_page_with_state(
        initialize_browser_state,
        playwright: Playwright
) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=STATE_PATH)
    yield context.new_page()
    browser.close()
