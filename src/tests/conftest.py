from playwright.sync_api import sync_playwright, Page
import pytest


@pytest.fixture(scope='session', name='page')
def chrome_page(request) -> Page:
    """
    Объект страницы браузера

    :return:
    """
    with sync_playwright() as pw:
        with pw.chromium.launch(headless=request.config.getoption('--headless')) as br:
            with br.new_context() as cont:
                with cont.new_page() as page:
                    yield page
