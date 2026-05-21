import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):  #playwright is a fixture provided by pytest - comes with pytest-playwright package
   browser = playwright.chromium.launch(headless=False)
   context= browser.new_context()
   page=context.new_page()
   page.goto("https://rahulshettyacademy.com/")

#page - itself is a fixture ,that suits only for chromium & edge engine headless=true mode, 1 single context only
def test_playwrightShort(page:Page):   #page is a fixture comes from Page(class) package - from playwright.sync_api import Page
   page.goto("https://rahulshettyacademy.com/")
   #configured --headed in run configurations

def test_playwrightCoreLocators(page: Page):
   page.goto("https://rahulshettyacademy.com/loginpagePractise/")
   page.get_by_label('Username:').fill('rahulshettyacademy')
   page.get_by_label('Password:').fill('Learning@830$3mK2')   #original pwd - Learning@830$3mK2
   page.get_by_role('combobox').select_option('teach')
   page.locator("#terms").check()  # CSS selectors using id #terms or .tagname, checking the checkbox
   page.get_by_role('button', name='Sign In').click()   #click signIn button
   expect(page.get_by_role('heading', name='Shop Name')).to_be_visible()


   # also page.get_by_role('link', name='terms and conditions' ).click()
   #page.pause() - to open playwright and see how it works
   #1. expect(page).to_have_url('https://rahulshettyacademy.com/angularpractice/shop')
   # verify login success
   # 🔹 OR Option 2
   #expect(page.get_by_text('Incorrect username/password.')).to_be_visible()    #wrong password check - negative test case
   #verify if dashboard is visible with correct credentials
   #auto wait mechanism for specific locators by playwright
   #time.sleep(3) - not needed as we have assertion here expect()

   #modify for firefox instance as well by creating a function
def test_playwrightFirefoxBrowser(playwright: Playwright):
   firefoxbrowser = playwright.firefox.launch(headless=False)
   page = firefoxbrowser.new_page()
   page.goto("https://rahulshettyacademy.com/loginpagePractise/")
   page.get_by_label('Username:').fill('rahulshettyacademy')
   page.get_by_label('Password:').fill('Learning@830$3mK2')  # original pwd - Learning@830$3mK2
   page.get_by_role('combobox').select_option('teach')
   page.locator("#terms").check()  # CSS selectors using id #terms or .tagname, checking the checkbox
   page.get_by_role('button', name='Sign In').click()  # click signIn button
   expect(page.get_by_role('heading', name='Shop Name')).to_be_visible()



