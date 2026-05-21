from .dashboard import DashboardPage

class LoginPage:
    #constructor
    def __init__(self, page):
        self.page = page    #this will have access to this entire page


    def navigate(self):
        # Wait for the initial page load to settle so Firefox does not continue while requests are still active.
        self.page.goto("https://rahulshettyacademy.com/client/", wait_until="networkidle")

    def login(self, useremail, userpassword):
        self.page.get_by_placeholder("email@example.com").fill(useremail)
        self.page.get_by_placeholder("enter your passsword").fill(userpassword)
        self.page.get_by_role("button", name="Login").click()
        # Wait until the dashboard is ready before the test clicks the ORDERS button.
        self.page.get_by_role("button", name="ORDERS").wait_for()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
