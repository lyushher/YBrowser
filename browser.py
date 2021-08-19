import json
import logging
import lxml.html
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay.smartdisplay import SmartDisplay

# For convenience
visible = EC.visibility_of_element_located
presence = EC.presence_of_element_located
clickable = EC.element_to_be_clickable


class Browser:
    def __init__(self, cookies_file='data/cookies.json', virtual_display=True, log_file=None):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            self.logger.addHandler(fh)

        self.cookies_file = cookies_file

        if virtual_display:
            self.display = SmartDisplay(visible=0, size=(1920, 1080))
            self.display.start()
        else:
            self.display = None

        self._reload_driver()

    def quit(self):
        if hasattr(self, 'driver'):
            self.clear_cookies()
            self.driver.quit()

    def save_cookies(self):
        self.logger.info('Saving cookies')
        cookies = self.driver.get_cookies()
        with open(self.cookies_file, 'w') as f:
            json.dump(cookies, f)

    def get_cookies(self):
        return self.driver.get_cookies()

    def load_cookies(self):
        # Note: to load cookies for a domain, you must
        # first navigate to that domain.
        self.logger.info('Loading cookies')
        try:
            with open(self.cookies_file, 'r') as f:
                cookies = json.load(f)
        except FileNotFoundError:
            return False
        for c in cookies:
            if isinstance(c.get('expiry'), float):
                c['expiry'] = int(c['expiry'])
            self.driver.add_cookie(c)
        return True

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def _reload_driver(self, opts=[]):
        self.quit()

        options = webdriver.ChromeOptions()
        for opt in opts:
            options.add_argument(opt)

        # Necessary for headless on server
        options.add_argument('--no-sandbox')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        # Don't ask to save passwords
        options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False
        })

        self.driver = webdriver.Chrome(chrome_options=options)
        self.wait = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)

    @property
    def user_agent(self):
        return self.driver.execute_script('return navigator.userAgent')

    def screenshot(self, fname=None):
        fname = fname or 'data/shots/{}.png'.format(datetime.utcnow().timestamp())
        if self.display:
            img = self.display.waitgrab()
            img.save(fname)
        else:
            self.driver.save_screenshot(fname)
        return fname

    def visit(self, url):
        self.driver.get(url)

    def input(self, selector, value, wait=True):
        if wait: self.wait.until(visible((By.CSS_SELECTOR, selector)))
        self.driver.find_element_by_css_selector(selector).send_keys(value)

    def click(self, selector, wait=True):
        if wait: self.wait.until(clickable((By.CSS_SELECTOR, selector)))
        self.driver.find_element_by_css_selector(selector).click()

    def select(self, selector, value):
        # Dropdowns
        select = Select(self.driver.find_element_by_css_selector(selector))
        select.select_by_value(value)

    def html(self):
        html = self.driver.find_element_by_tag_name('html').get_attribute('innerHTML')
        return lxml.html.fromstring(html)

    def wait_for(self, selector):
        self.wait.until(visible((By.CSS_SELECTOR, selector)))

    @property
    def url(self):
        return self.driver.current_url
