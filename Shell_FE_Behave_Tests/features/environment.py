import os
import shutil
import sys
import time

import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Azure_Test_Result_update import TestResultUpdate
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities


def before_all(context):
    SeleniumBase.initialize_values()
    SeleniumBase.browser_initialization()


def before_feature(context, feature):
    # for scenario in feature.scenarios:
    #     patch_scenario_with_autoretry(scenario, max_attempts=2)
    pass


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return


def after_step(context, step):
    if step.status == "failed":
        screenshot_name = str(context.scenario.name).replace(" ", "_")
        BrowserUtilities.take_screenshot(screenshot_name)


def after_feature(context, feature):
    """The below code is used to mark the test results in Browserstack as passed or failed based on the assertions
    validated. Can be commented out or removed if in case Browserstack execution is not performed"""
    # if context.failed is True:
    #     SeleniumBase.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At '
    #         'least 1 assertion failed"}}')
    # if context.failed is not True:
    #     SeleniumBase.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All '
    #         'assertions passed"}}')


def after_scenario(context, scenario):
    # For UI automation
    config = SeleniumBase.read_config()
    azure_value = config.getboolean('Azure_Test_plan', 'update_result')
    if scenario.status == "failed":
        if "web" in context.feature.tags:
            allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
        if azure_value:
            for tag in context.scenario.tags:
                try:
                    print(tag)
                    pid = int(tag)
                    if "int" in str(type(pid)):
                        dictionary = {pid: "failed"}
                        FileUtilities.append_dictionary_into_json(dictionary,
                                                                  f"{config['azure_test_result']['filename']}")
                        BrowserUtilities.log.info("Test case ID and status value:" + str(dictionary))
                except:
                    pass

    elif scenario.status == "passed":
        if azure_value:
            for tag in context.scenario.tags:
                try:
                    print(tag)
                    pid = int(tag)
                    if "int" in str(type(pid)):
                        dictionary = {pid: "passed"}
                        FileUtilities.append_dictionary_into_json(dictionary,
                                                                  f"{config['azure_test_result']['filename']}")
                        BrowserUtilities.log.info("Test case ID and status value:" + str(dictionary))
                except:
                    pass


def after_all(context):
    # Push the history folder to Allure reports
    # current_directory = os.path.dirname(os.getcwd())
    # src_directory = current_directory + "/Shell_FE_Behave_Tests/TestResults/Reports/history/"
    # dst_directory = current_directory + "/Shell_FE_Behave_Tests/TestResults/AllureJson/history/"
    # all_files = os.listdir(src_directory)
    # for file in all_files:
    #     shutil.move(src_directory + file, dst_directory + file)

    SeleniumBase.dispose()

    # region Updating result to the Azure Test plan
    config = SeleniumBase.read_config()
    azure_value = config.getboolean('Azure_Test_plan', 'update_result')
    file_name = config['azure_test_result']['filename']
    time.sleep(10)
    if azure_value:
        # file_name - name of the file, that you have declared in the behave.ini
        TestResultUpdate.test_plan_result_update(file_name)
        FileUtilities.copy_file_to_directory(f"{file_name}", f"AzureTestResultHistory/{file_name}")
        FileUtilities.delete_file(f"{file_name}")
    # endregion
