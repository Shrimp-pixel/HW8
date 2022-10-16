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
@allure.feature('Проверка issue с steps')
@allure.story("Нахождение вкладки issue")
@allure.link('https://github.com', name='Testing')
def test_issue_steps():
    open_page('https://github.com')

    find_repo('eroshenkoam/allure-example')

    click_repo('eroshenkoam/allure-example')

    click_tab('#issues-tab')

    find_issue('#81')


@allure.step('Открываем страницу')
def open_page(url):
    browser.open(url)


@allure.step("Ищем репозиторий {repo}")
def find_repo(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step("Нажимаем на найденный {repo}")
def click_repo(repo):
    s(by.link_text(repo)).click()


@allure.step("Нажимаем на вкладку")
def click_tab(tab):
    s(tab).click()


@allure.step("Проверяем отображение элемента")
def find_issue(issue):
    s(by.partial_text(issue)).should(be.visible)
