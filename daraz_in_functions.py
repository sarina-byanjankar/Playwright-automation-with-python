from playwright.sync_api import sync_playwright


def launch_browser():
    """Launch browser and return page object"""
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    return p, browser, page


def search_product(page, product_name):
    """Search for a product"""
    page.goto("https://www.daraz.com.np")
    page.fill("input[name='q']", product_name)
    page.click(".search-box__button--1oH7")
    # wait for results
    page.wait_for_selector("a[href*='/products/']")


def click_first_product(page):
    """Click the first product in results"""
    page.locator("a[href*='/products/']").first.click()


def handle_popup(page):
    """Handle popup if it appears"""
    try:
        page.wait_for_selector(".popup-class", timeout=5000)
        page.locator(".popup-class .button-class").click()
    except:
        print("Popup did not appear, continuing...")


def close_browser(p, browser):
    """Close browser and Playwright"""
    browser.close()
    p.stop()

# -------------------------
# Main automation
# -------------------------


def main():
    p, browser, page = launch_browser()
    try:
        search_product(page, "laptop")
        click_first_product(page)
        handle_popup(page)
        # optionally scroll
        # page.mouse.wheel(0, 3000)
    finally:
        close_browser(p, browser)


if __name__ == "__main__":
    main()
