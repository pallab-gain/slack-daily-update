from selenium.webdriver.support.wait import WebDriverWait
from browser.browser import Browser
import argparse
import time


def signin(chrome=None, url=None, email=None, password=None):
    if not (chrome and url and email and password):
        return

    chrome.get(url)
    WebDriverWait(chrome, 10).until(
        lambda _chrome_browser: chrome.find_element_by_id("signin_btn"))

    email = chrome.find_element_by_id("email")
    password = chrome.find_element_by_id("password")
    signing_button = chrome.find_element_by_id("signin_btn")

    email.clear()
    email.send_keys(email)
    password.clear()
    password.send_keys(password)
    signing_button.click()


def select_channel(chrome=None, channel=None):
    if not (chrome and channel):
        return False
    WebDriverWait(chrome, 30).until(
        lambda _chrome_browser: chrome.find_elements_by_css_selector(".p-channel_sidebar__channel"))

    for element in chrome.find_elements_by_css_selector(".p-channel_sidebar__channel"):
        if channel in element.text:
            element.click()
            return True

    return False


def submit(chrome=None, message=None):
    if not (chrome and message):
        return False

    textbox = chrome.find_element_by_css_selector("#msg_input  p")
    chrome.execute_script("arguments[0].textContent = arguments[1];", textbox, message)
    onsubmit = chrome.find_element_by_id("msg_form")
    onsubmit.submit()

    return True


def get_message():
    from data import loadpath as filepath
    _filepath = filepath.load_path()
    msg = time.strftime("*Update %d/%m:*")+"\n"

    with open(_filepath) as fd:
        itr = 1
        for line in fd.readlines():
            msg = msg + str(itr)+ ". "+line
            itr +=1

    return msg

def main(args):
    slackurl = args.slackurl
    channel = args.channel
    email = args.email
    password = args.password
    message = get_message()

    # print message
    browser = Browser()

    chrome = browser.get_browser()
    signin(chrome=chrome, url=slackurl, email=email, password=password)
    select_channel(chrome=chrome, channel=channel)
    submit(chrome=chrome, message=message)

    browser.dispose(browser=chrome)


# email
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='App that post daily updates to slack group')

    parser.add_argument('-slackurl', '-s', help="slack url", required=True, dest='slackurl')
    parser.add_argument('-channel', '-c', help="channel", required=True, dest='channel')
    parser.add_argument('-email', '-e', help="email", required=True, dest='email')
    parser.add_argument('-password', '-p', help="password", required=True, dest='password')

    args = parser.parse_args()
    main(args)
