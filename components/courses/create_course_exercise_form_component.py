from playwright.sync_api import expect

from components.base_component import BaseComponent


class CreateCourseExerciseFormComponent(BaseComponent):
    # Локаторы динамические (зависят от index), поэтому пока объявляем их в методах
    def click_delete_button(self, index: int):
        delete_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_button.click()

    def check_visible(self, index: int, title: str, description: str):
        subtitle = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input").locator('input')
        description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator('input')

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill(self, index: int, title: str, description: str):
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input").locator('input')
        description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator('input')

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)
