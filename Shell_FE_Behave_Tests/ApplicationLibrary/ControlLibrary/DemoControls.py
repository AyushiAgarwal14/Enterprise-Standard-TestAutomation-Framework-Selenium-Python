from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities


class DemoControls:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "idToken1")
    password = (By.ID, "idToken2")
    login_button = (By.ID, "loginButton_0")
    remember_password_checkbox = (By.XPATH, "//*[contains(text(),'Remember')]")
    india_flag = (By.XPATH, "//*[text()='India']")
    download_btn = (By.XPATH,"//a[text()='Download']")

    def get_download_btn(self):
        return self.driver.find_element(*DemoControls.download_btn)

    def get_country_flag_element(self):
        return self.driver.find_element(*DemoControls.india_flag)

    def get_email_text_box(self):
        return self.driver.find_element(*DemoControls.username)

    def get_password_text_box(self):
        password_text_box = SeleniumUtilities.get_element_with_relative_locators(self.get_email_text_box(), "input",
                                                                                 "below")
        return password_text_box

    def get_remember_password_checkbox(self):
        return SeleniumUtilities.get_element_with_relative_locators(self.get_password_text_box(), "input", "below")

    def get_login_button(self):
        return self.driver.find_element(*DemoControls.login_button)

    def get_password_with_relative_locators(self):
        return SeleniumUtilities.get_element_with_relative_locators(self.get_login_button(), "input", "above")

    def get_remember_password_option(self):
        return self.driver.find_element(*DemoControls.remember_password_checkbox)

    def get_forgot_password_option(self):
        return SeleniumUtilities.get_element_with_relative_locators(self.get_remember_password_option(), "a",
                                                                    "to_right_of")
