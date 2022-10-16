from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest
import allure
from allure_commons.types import Severity


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.config.window_height = 1200
    browser.config.window_width = 1200


@allure.tag('web')
@allure.label(Severity.BLOCKER)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка issue с with')
@allure.story("Нахождение вкладки issue")
@allure.link('https://github.com', name='Testing')
def test_issue_with():
    with allure.step('Открываем страницу'):
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий"):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step("Нажимаем на найденный репозиторий"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Нажимаем на вкладку"):
        s('#issues-tab').click()

    with allure.step("Проверяем отображение элемента"):
        s(by.partial_text('#81')).should(be.visible)



