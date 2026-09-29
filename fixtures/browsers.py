import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

BASE_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course'
REGISTRATION_URL = f'{BASE_URL}/#/auth/registration'
STATE_PATH = 'browser-state.json'


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    # request.node.name - имя текущего автотеста, по нему называем файл трейсинга
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(REGISTRATION_URL)
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    # Дожидаемся редиректа на Dashboard, чтобы состояние сохранилось уже после регистрации
    dashboard_page = DashboardPage(page=page)
    dashboard_page.dashboard_toolbar_view.check_visible()

    context.storage_state(path=STATE_PATH)
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=STATE_PATH)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
