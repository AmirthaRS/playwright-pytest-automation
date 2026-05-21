import pytest


@pytest.fixture(scope='session')
def user_credentials(request):   #global request parameter in pytest
    return request.param

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection"
                     )
    parser.addoption("--url_name", action="store", default="https://rahulshettyacademy.com/client/", help="url selection"
                     )

# Use function scope so each parametrized test gets a fresh page instead of reusing a page that may be closed.
@pytest.fixture(scope='function')
def browserInstance(request, playwright):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        # Fail clearly if pytest is run with a browser name this fixture does not support.
        raise ValueError(f"Unsupported browser_name: {browser_name}")

    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    #page.goto(url_name)
    yield page
    context.close()
    browser.close()
