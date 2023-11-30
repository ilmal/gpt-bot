"""
the cookie expire is weird

run the code and if exception just clear cookies and start the login process again

"""


from selenium import webdriver
import time


from get_browser import get_browser
from get_element import get_element # takes in (driver, input, search_type="XPATH")

def main():
    url = "https://chat.openai.com/auth/login"

    browser = get_browser()

    browser.get(url)

    login_button = get_element(browser, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]")
    login_button.click()

    time.sleep(50)

    browser.quit()


if __name__ == "__main__":
    main()