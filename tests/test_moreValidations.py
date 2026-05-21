from playwright.sync_api import Page, expect


#placeholder
# noinspection PyGlobalUndefined
def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()

    #alerts handling - alerts - not html handled -non web.. JS
    page.on("dialog", lambda dialog: dialog.accept())  #accept whenever a dialog appears here #error - IDE
    page.locator("#confirmbtn").click()

    #frame handling - embedded with parent html page - ex: magazines
    #manually switch to specific iframes and handle it.
    pageFrame = page.frame_locator(
        '#courses-iframe')  # cannot use page object here , use pageFrame to work with elements in that frame
    pageFrame.get_by_role('link', name='Learning paths').click()
    expect(pageFrame.locator(".text",
                             has_text='A Learning Path is a selection of courses tied together for learners')).to_be_visible()

    #working with html tables
    #check price of strawberry is 23
    #switching to page object which points to normal page rather than iframes page
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    #using nth()
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColvalue: int = index
            print(f'Pricecolvalue is: {priceColvalue}')
            break

    ricerow = page.locator("tr").filter(has_text="Rice")
    expect(ricerow.locator("td").nth(priceColvalue)).to_have_text("37")
    #print(priceColvalue)
