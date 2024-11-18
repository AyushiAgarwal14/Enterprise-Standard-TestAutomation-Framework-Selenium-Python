import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.ResourceContextControls import ResourceContextControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.AccessibilityUtilities import AccessibilityUtilities
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities

class F2:

    def __init__(self):
        self.Test_Control = ResourceContextControls(SeleniumBase.driver)

    def access_Rs1(self):
        BrowserUtilities.navigate_to_url(SeleniumBase.url)
        BrowserUtilities.maximize_window()
        #BrowserUtilities.resize_browser(1920, 1080)
        BrowserUtilities.refresh_page()

    def click_context_dropdown(self):
        time.sleep(10)
        SeleniumUtilities.click_element(self.Test_Control.Context_dropdown())
    def click_Resource_context(self):
        SeleniumUtilities.click_element(self.Test_Control.Resource_context())
        time.sleep(2)
    def click_Report_group(self):
        SeleniumUtilities.click_element(self.Test_Control.Report_group())
        time.sleep(2)
    def click_ARPR_reports(self):
        SeleniumUtilities.click_element(self.Test_Control.ARPR_reports())
        time.sleep(2)
    def click_SUM_reports(self):
        SeleniumUtilities.click_element(self.Test_Control.SUM_reports())
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
    def click_Report_option(self):
        SeleniumUtilities.click_element(self.Test_Control.Report_option())
        time.sleep(2)      
    def click_Node(self):
        SeleniumUtilities.click_element(self.Test_Control.Node()) 
        time.sleep(20)     
    


    #R06 Reports


    def click_R06_01_SECP_Reserves_report(self):
        SeleniumUtilities.click_element(self.Test_Control.R06_01_SECP_Reserves_report())
        time.sleep(2)
    def click_R06_02_2P_Reserves_report(self):
        SeleniumUtilities.click_element(self.Test_Control.R06_02_2P_Reserves_report())
        time.sleep(2)
    def click_R06_03_3P_Reserves_report(self):
        SeleniumUtilities.click_element(self.Test_Control.R06_03_3P_Reserves_report())
        time.sleep(2)
    def click_R06_04_2C_Reserves_report(self):
        SeleniumUtilities.click_element(self.Test_Control.R06_04_2C_Reserves_report())
        time.sleep(2)
    def click_R06_05_2U_Reserves_report(self):
        SeleniumUtilities.click_element(self.Test_Control.R06_05_2U_Reserves_report())
        time.sleep(2)
      

    def click_Subtotalling_selected(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Subtotalling_selected())
        time.sleep(2)
    def click_Subtotalling_Attributes(self):
        SeleniumUtilities.unselect_checkbox(self.Test_Control.Subtotalling_Attributes())
        time.sleep(2)      
    def click_Subtotalling_objects(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Subtotalling_objects()) 
        time.sleep(20)     
    
    
    
    #R01 Reports

    
    def click_R01_08_SUMANREV_Liquids(self):
        SeleniumUtilities.click_element(self.Test_Control.R01_08_SUMANREV_Liquids())
        time.sleep(2)
    def click_R01_09_SUMANREV_Gas(self):
        SeleniumUtilities.click_element(self.Test_Control.R01_09_SUMANREV_Gas())
        time.sleep(2)
    def click_R01_10_SUMANREV_BOE(self):
        SeleniumUtilities.click_element(self.Test_Control.R01_10_SUMANREV_BOE())
        time.sleep(2)
    def click_R01_11_SUMANREV_Indicators(self):
        SeleniumUtilities.click_element(self.Test_Control.R01_11_SUMANREV_Indicators())
        time.sleep(2)
    def click_R01_12_SUMANREV_indicators_Liquids(self):
        SeleniumUtilities.click_element(self.Test_Control.R01_12_SUMANREV_indicators_Liquids())
        time.sleep(2)
    def click_R01_13_SUMANREV_indicators_Gas(self):
        SeleniumUtilities.click_element(self.Test_Control.R01_13_SUMANREV_indicators_Gas())
        time.sleep(2)
    def click_R01_14_SUMANREV_indicators_BOE(self):
        SeleniumUtilities.click_element(self.Test_Control.R01_14_SUMANREV_indicators_BOE())
        time.sleep(2)


    def click_Units_1column(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Units_1column(), 'Metric')
        time.sleep(2)   
    def click_Units_2column(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Units_2column(), 'Medium')
        time.sleep(2)