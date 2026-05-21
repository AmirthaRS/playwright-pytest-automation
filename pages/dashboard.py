from .ordersHistory import OrdersHistoryPage

class DashboardPage:
    # constructor
    def __init__(self, page):
        self.page = page  # this will have access to this entire page

    def selOrdernavigationLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordersHistoryPage = OrdersHistoryPage(self.page)
        return ordersHistoryPage
