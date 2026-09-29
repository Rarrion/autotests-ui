from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page(base_url=settings.get_base_url())

    page.goto(AppRoute.REGISTRATION)

    registration_button = page.get_by_test_id(
        'registration-page-registration-button'
    )
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id(
        'registration-form-email-input'
    ).locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id(
        'registration-form-username-input'
    ).locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id(
        'registration-form-password-input'
    ).locator('input')
    password_input.fill(settings.test_user.password)

    expect(registration_button).to_be_enabled()

    browser.close()
