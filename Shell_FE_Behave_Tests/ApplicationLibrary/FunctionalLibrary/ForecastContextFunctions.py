import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.ForecastContextControls import ForecastContextControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.AccessibilityUtilities import AccessibilityUtilities
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

class F1:

    def __init__(self):
        self.Test_Control = ForecastContextControls(SeleniumBase.driver)

    def access_Rs1(self):
        BrowserUtilities.navigate_to_url(SeleniumBase.url)
        BrowserUtilities.maximize_window()
        #BrowserUtilities.resize_browser(1920, 1080)
        BrowserUtilities.refresh_page()

    def click_context_dropdown(self):
        time.sleep(10)
        SeleniumUtilities.click_element(self.Test_Control.Context_dropdown())
    def click_forecast_context(self):
        SeleniumUtilities.click_element(self.Test_Control.Forecast_context())
        time.sleep(2)
    def click_Report_group(self):
        SeleniumUtilities.click_element(self.Test_Control.Report_group())
        time.sleep(2)
    def  click_ARPR_reports(self):
        SeleniumUtilities.click_element(self.Test_Control.ARPR_reports())
        time.sleep(2)
    def click_Report_dropdown(self):
        SeleniumUtilities.click_element(self.Test_Control.Report_dropdown())
        time.sleep(2)
    def click_hierarchy_dropwdown(self):
        SeleniumUtilities.click_element(self.Test_Control.Hierarchy_dropdown())
        time.sleep(2)
    def click_AoO_LoB_Field(self):
        SeleniumUtilities.click_element(self.Test_Control.AoO_LoB_Field())
        time.sleep(2)
    def click_version(self):
        SeleniumUtilities.click_element(self.Test_Control.Version())
        time.sleep(2)
    def  click_ARPR_version(self):
        SeleniumUtilities.click_element(self.Test_Control.ARPR_version())
        time.sleep(2)
    def click_filter(self):
        SeleniumUtilities.click_element(self.Test_Control.Filter())
        time.sleep(2)
    def click_No_filter(self):
        SeleniumUtilities.click_element(self.Test_Control.No_filter())
        time.sleep(2)
    def click_Report_header(self):
        SeleniumUtilities.click_element(self.Test_Control.Report_header())
        time.sleep(2)
    def click_Report_viewer(self):
        SeleniumUtilities.click_element(self.Test_Control.Report_viewer())
        time.sleep(2)
    def click_Report_option  (self):
        SeleniumUtilities.click_element(self.Test_Control.Report_option())
        time.sleep(2)      
    def click_Node (self):
        SeleniumUtilities.click_element(self.Test_Control.Node()) 
        time.sleep(20)     
    


    #Contract Report

    def click_Contract_report(self):
        SeleniumUtilities.click_element(self.Test_Control.Contract_Report())
        time.sleep(2)
    def click_Report_type(self):
        SeleniumUtilities.select_radiobutton(self.Test_Control.Report_type_Allcontracts())
        time.sleep(2)
    def click_Include_old_contract_details(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Include_old_contract_details_Yes())
        time.sleep(2)
    def click_Include_objectives(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Include_Objectives_Yes())
        time.sleep(2)
    def click_units(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Units_1000(), '1000 acres')
        time.sleep(2)


    



    