# importing playwright, it loads the playwright library
from playwright.sync_api import sync_playwright

with sync_playwright() as p:  # starts the browser
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.daraz.com.np")
    # using CSS selector to type "laptop" in the search box
    page.type("input[name='q']", "laptop")
    
    
    # using class selector to click the search button
    page.click(".search-box__button--1oH7")
    # clicking on first product on the list from the respective class
    page.locator(".picture-wrapper.jBwCF ").first.click()
    # waits for the page to load completely
    page.mouse.wheel(0, 1000)  # scrolls down the page
    page.click(".next-icon.next-icon-add.next-icon-medium")
    page.click("text=Add to Cart")

    # accepts the alert dialog
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator("text=Phone Number").click()

    # waits for user input before closing the browser
    input("Press Enter to close the browser...")
    # print(page.title())
