from typing import Generator
from selenium import webdriver
from selenium.webdriver import Safari
import pytest


@pytest.fixture
def browser() -> Generator[Safari, None, None]:
    browser = webdriver.Safari()
    yield browser
    browser.quit()


def test_can_start_a_list_and_retrieve_it_later(browser):
    browser.get('http://localhost:8000')

    assert "To-Do" in browser.title
