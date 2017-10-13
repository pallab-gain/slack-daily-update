from selenium.webdriver.support.wait import WebDriverWait
from browser.browser import Browser
import argparse
import time


def signin(chrome=None, url=None, email=None, password=None):
    print 'signing in ...'

    if not (chrome and url and email and password):
        return

    chrome.get(url)
    WebDriverWait(chrome, 10).until(
        lambda _chrome_browser: chrome.find_element_by_id("signin_btn"))

    email_elem = chrome.find_element_by_id("email")
    password_elem = chrome.find_element_by_id("password")
    signing_button = chrome.find_element_by_id("signin_btn")

    email_elem.clear()
    email_elem.send_keys(email)
    password_elem.clear()
    password_elem.send_keys(password)
    signing_button.click()


def select_channel(chrome=None, channel=None):
    print 'selecting channel ...'
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
    print 'submitting text ... '
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


    browser = Browser()

    # display = browser.get_display()
    # display.start()

    chrome = browser.get_browser()
    signin(chrome=chrome, url=slackurl, email=email, password=password)
    if select_channel(chrome=chrome, channel=channel):
        submit(chrome=chrome, message=message)

    time.sleep(5)
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
