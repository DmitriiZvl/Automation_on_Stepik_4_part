import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en',
                     help="Choose language browser: ru,en,es... (default - en)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    
    if browser_name == "chrome":
        EXoptions = Options()
        EXoptions.add_experimental_option('prefs', {'intl.accept_languages':language})
        browser = webdriver.Chrome(options=EXoptions)
        
        print("\n==========Start Chrome browser for test..==========")
        
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        
        print("\nStart Firefox browser for test..")
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n==========quit browser..==========")
    
    browser.quit()

    
