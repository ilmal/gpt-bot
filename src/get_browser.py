from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_browser():
    options = Options()
    options.log.level = 'trace'

    browser = webdriver.Firefox(options=options)

    return browser