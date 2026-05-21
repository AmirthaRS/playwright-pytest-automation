import re

from playwright.sync_api import Page, expect

#important concepts#

def test_UIValidations(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('Learning@830$3mK2')
    page.get_by_role('combobox').select_option('teach')
    page.locator("#terms").check()
    page.get_by_role('button', name='Sign In').click()   #getbyrole has 2 parameters that it will take
    page.locator("#login").click()

    iphonecard = page.locator('app-card').filter(has_text='iphone X')
    iphonecard.get_by_role('button').click()
    nokiacard = page.locator('app-card').filter(has_text='Nokia Edge')  #locator has filter() option externally
    nokiacard.get_by_role('button').click()
    page.get_by_text('Checkout').click()   #getbytext has partial text on the page as well
    expect(page.locator(".media-body")).to_have_count(2)  #using dot for CSS selectors

def test_childWindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    #closure
    with page.expect_popup() as newPageInfo:
        #step1..2..
        page.locator(".blinkingText").get_by_text("Free Access").click()  # use selectorhub plugin to check CSS selectors
        childPage = newPageInfo.value    #newpageInfo object gets invoked here
        text=childPage.locator(".red").text_content()
        print(text)
        #email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text).group() #using regular expression
        #print(email)
        words=text.split("at")
        email=words[1].strip().split(' ')[0]
        print(email)
        assert email == 'mentor@rahulshettyacademy.com'



        #text - Please email us at mentor@rahulshettyacademy.com with below template to receive response




