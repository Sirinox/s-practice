"""
Проверка браузерного калькулятора google.
"""
from playwright.sync_api import expect


def test_google_calc(page):
    """
    Проверка доступности браузерного калькулятора google через поиск.
    Проверка корректного счета.

    :param page:
    :return:
    """
    # ARRANGE
    page.goto('http://google.com')

    # ACT
    page.locator('(//textarea)[1]').fill('Калькулятор')
    page.get_by_text('Поиск в Google').first.click()
    calc_frame = page.locator(selector='//*[@id="cwos"]')
    calc_frame.click()
    calc_frame.type('1*2-3+1', delay=150)
    page.keyboard.press('Enter')

    # ASSERT
    expect(calc_frame).to_contain_text('0', timeout=1_000)
