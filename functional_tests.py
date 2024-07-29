import time
from typing import Generator
from selenium import webdriver
from selenium.webdriver import Safari
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser() -> Generator[Safari, None, None]:
    browser = webdriver.Safari()
    yield browser
    browser.quit()


def test_can_start_a_list_and_retrieve_it_later(browser):
    browser.get('http://localhost:8000')

    assert "To-Do" in browser.title
    header_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert 'To-Do' in header_text
    
    input_box = browser.find_element(By.ID, 'id_new_item')
    assert input_box.get_attribute('placeholder') == 'Enter a to-do item'
    
    input_box.send_keys('Buy peacock feathers')
    
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)
    
    table = browser.find_element(By.ID, 'id_list_table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    assert any(row.text == '1: Buy peacock feathers' for row in rows)

