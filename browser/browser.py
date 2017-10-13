from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

# local import
from driver import loadpath as driver


class Browser():
    def __init__(self):
        self._display = None
        self._chrome_browser = None

    def get_display(self):
        display = Display(visible=0, size=[640, 480])
        return display

    def get_browser(self):
        chrome_option = Options()
        chrome_browser = webdriver.Chrome(executable_path=driver.load_path(), chrome_options=chrome_option)
        return chrome_browser

    def dispose(self, browser=None, display=None):
        if browser:
            browser.quit()

        if display:
            display.stop()
