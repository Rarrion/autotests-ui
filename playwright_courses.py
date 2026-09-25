from playwright.sync_api import sync_playwright, expect

BASE_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course'
REGISTRATION_URL = f'{BASE_URL}/#/auth/registration'
COURSES_URL = f'{BASE_URL}/#/courses'
STATE_PATH = 'browser-state.json'

with sync_playwright() as playwright:
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

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()

    context.storage_state(path=STATE_PATH)

    new_context = browser.new_context(storage_state=STATE_PATH)
    new_page = new_context.new_page()

    new_page.goto(COURSES_URL)

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
