from playwright.sync_api import sync_playwright


def search_product(page, product_name):
    page.goto("https://www.daraz.com.np", timeout=60000)
    page.type("input[name='q']", product_name)
    page.click(".search-box__button--1oH7")


def select_first_product(page):
    page.locator(".picture-wrapper.jBwCF").first.click()


def scroll_and_add_to_cart(page):
    page.mouse.wheel(0, 1000)  # scroll down
    page.click(".next-icon.next-icon-add.next-icon-medium")
    page.click("text=Add to Cart")


def handle_dialog(page):
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator("text=Phone Number").click()


# function to lanch the browser and execute the steps
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        search_product(page, "laptop")
        select_first_product(page)
        scroll_and_add_to_cart(page)
        handle_dialog(page)

        input("Press Enter to close the browser...")


# using main() will only allow the code to run when this file is executed directly,and if imported the main will still run atuomatically.
main()

# the following will allow the code to run when this file is executed directly, and not when imported as a module
# if __name__ == "__main__":
#     main()
