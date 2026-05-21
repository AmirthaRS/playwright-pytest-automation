#testing edge cases
#network interception - intercepting responses, intercepting requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from playwright.sync_api import Page, expect, Playwright
from utils.apiBase import APIUtils

def intercept_request(route):
    route.continue_(url ="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69e62b74f86ba51a6576422c")
    #this order id is taken from other account for this concept - anu6@gmail.com , 13Bcs008***
    #which invalidates the order id resulting in non authorization


def test_Network(page:Page):
    # login
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*" , intercept_request)  #on clicking view button
    page.get_by_placeholder("email@example.com").fill("rsddamirtha@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("13Bcs007***")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()   #line 14 is provoked here
    #time.sleep(5)
    message= page.locator(".blink_me").text_content()
    print(message)  #You are not authorize to view this order

def test_session_storage(playwright: Playwright):
    api_utils= APIUtils()
    getToken = api_utils.getToken(playwright)
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page= context.new_page()
    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem("token", "{getToken}")""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()

