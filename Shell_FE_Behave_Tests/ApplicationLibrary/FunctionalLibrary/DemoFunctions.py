import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.DemoControls import DemoControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities


class DemoFunctions:

    def __init__(self):
        self.demoControls = DemoControls(SeleniumBase.driver)

    def navigate_to_url(self):
        BrowserUtilities.navigate_to_url(SeleniumBase.url)

    def click_download_btn(self):
        SeleniumUtilities.click_element(self.demoControls.get_download_btn())


    def send_text_to_username(self):
        WaitUtilities.wait_for_element_to_be_visible(self.demoControls.username)
        SeleniumUtilities.send_text(self.demoControls.get_email_text_box(), "SauceLabs")

    def send_text_to_password(self):
        SeleniumUtilities.send_text(self.demoControls.get_password_text_box(), "saucelabs")

    def click_forgot_password(self):
        SeleniumUtilities.click_element(self.demoControls.get_forgot_password_option())

    def open_new_tab(self):
        BrowserUtilities.switch_to_new_tab()
        SeleniumBase.driver.get("https://www.google.com/")

    def open_new_window(self):
        BrowserUtilities.switch_to_new_window()
        SeleniumBase.driver.get("https://www.lambdatest.com/")

    def enter_user_name_with_action_class(self):
        SeleniumUtilities.click_element(self.demoControls.get_email_text_box())
        SeleniumUtilities.send_text_to_focused_element_by_actions("Selenium Demo")

    def enter_password_with_action_class(self):
        SeleniumUtilities.send_text_by_actions(self.demoControls.get_password_text_box(), "Selenium")
        time.sleep(3)

    def click_login_button_with_action_class(self):
        SeleniumUtilities.click_element_by_actions(self.demoControls.get_login_button())

    def scroll_to_element_with_action_class(self):
        SeleniumUtilities.switch_to_new_tab()
        SeleniumBase.driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
        time.sleep(2)
        SeleniumUtilities.scroll_to_element_by_actions(self.demoControls.get_country_flag_element())
        time.sleep(2)
        SeleniumUtilities.scroll_by_amount_actions(0, 200)
        time.sleep(2)
        scrollOrigin = ScrollOrigin.from_element(self.demoControls.get_country_flag_element())
        SeleniumUtilities.scroll_from_an_element_by_a_given_amount_by_actions(scrollOrigin, 0, 500)
        time.sleep(3)
