#testing edge cases
#network interception - intercepting responses, intercepting requests
from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json= fakePayloadOrderResponse)

def test_Network(page:Page):
    # login
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*" , intercept_response)
    page.get_by_placeholder("email@example.com").fill("rsddamirtha@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("13Bcs007***")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()  #line 14 is provoked here
    order_text= page.locator(".mt-4").text_content()
    print(order_text)
    #event handler - route() #no orders made

