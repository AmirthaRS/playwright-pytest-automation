#API testing e2e  - e-commerce website
#API and UI testing - login and create an order
#use selectorshub plugin in browser tools
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils
from pages.login import LoginPage

def test_endtoend_web_api(playwright: Playwright):   #user_credentails is a fixture here which is linked to parameter user_credentials
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    #create order - order id
    apiUtils = APIUtils()
    orderId = apiUtils.createOrder(playwright)  #user credentials linked here to create order method in API class

    #login POM changes #commented lines 30-33 are before POM
    #loginPage= LoginPage(page)  #page object parameter also compatible with constructor
    #loginPage.navigate()
    #loginPage.login(useremail, userpassword)
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rsddamirtha@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("13Bcs007***")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()

    #IMPORTANT: using same playwright instance throughout the API scenario

    #test case - order history page - after login: check order is present after createorder using API
    #logic to check that
    row= page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button" , name= "View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print("Thank you for Shopping With Us")
    context.close()
















#network intercepting - automating edge case scenario - no orders - route method