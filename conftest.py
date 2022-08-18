import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choosing correct language for the site")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nUsing " + str(language) + " for test.")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nQuit browser...")
    browser.quit()
