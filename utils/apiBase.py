from playwright.sync_api import Playwright

#from playwright.conftest import user_credentials

payloadData = {"orders":[{"country":"Albania","productOrderedId":"6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self, playwright: Playwright):
        #user_email = user_credentials["userEmail"]
        #user_password = user_credentials["userPassword"]
        login_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        response = login_context.post("/api/ecom/auth/login",
                           data={"userEmail": "rsddamirtha@gmail.com","userPassword": "13Bcs007***"}
                           )
        assert response.ok
        token = response.json()["token"]
        return token

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        response= api_context.post("/api/ecom/order/create-order",
                         data =payloadData,
                         headers = {
                             "Authorization": token,
                             "Content-Type": "application/json"
                                    }
                         )
        print(response.json())
        responseBody= response.json()
        orderID = responseBody["orders"][0]
        return orderID
