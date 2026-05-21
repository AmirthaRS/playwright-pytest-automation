#API testing e2e  - e-commerce website
#API and UI testing - login and create an order
#use selectorshub plugin in browser tools
#pytest --browser_name chrome -m smoke -n 3 --tracing on --html=report.html #terminal run
import sys
import os
import json , pytest
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "")))
from playwright.sync_api import Playwright, expect
from utils.apiBaseFramework import APIUtils
from pages.login import LoginPage

# json file - util - accessing into test
credentials_path = Path(__file__).parent.parent / "data" / "credentials.json"
with open(credentials_path) as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']  # accessing json values

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_endtoend_web_api(playwright: Playwright, browserInstance, user_credentials):
    #user_credentails is a fixture here which is linked to parameter user_credentials_list
    useremail = user_credentials["userEmail"]
    userpassword = user_credentials["userPassword"]
    #browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context(ignore_https_errors=True)
    #page = context.new_page()

    #create order - order id
    apiUtils = APIUtils()
    orderId = apiUtils.createOrder(playwright, user_credentials)  #user credentials linked here to create order method in API class

    #login POM changes #commented lines 30-33 are before POM
    loginPage= LoginPage(browserInstance)  #page object parameter also compatible with constructor in login.py under pages
    #browerInstance is a fixure that returns actual page object to the Loginpage Class
    loginPage.navigate()
    dashboardPage = loginPage.login(useremail, userpassword)
    orderHistoryPage = dashboardPage.selOrdernavigationLink()
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.displayOrderMessage()
    #context.close()
    #page object design pattern created successfully
















#network intercepting - automating edge case scenario - no orders - route method
