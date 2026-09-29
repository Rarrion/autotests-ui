from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)

    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

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

    registration_button = page.get_by_test_id(
        'registration-page-registration-button'
    )
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()

    context.storage_state(path=settings.browser_state_file)

    new_context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=settings.browser_state_file
    )
    new_page = new_context.new_page()

    new_page.goto(AppRoute.COURSES)

    courses_title = new_page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    empty_view_title = new_page.get_by_test_id(
        'courses-list-empty-view-title-text'
    )
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')

    empty_view_icon = new_page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    empty_view_description = new_page.get_by_test_id(
        'courses-list-empty-view-description-text'
    )
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text(
        'Results from the load test pipeline will be displayed here'
    )

    browser.close()
