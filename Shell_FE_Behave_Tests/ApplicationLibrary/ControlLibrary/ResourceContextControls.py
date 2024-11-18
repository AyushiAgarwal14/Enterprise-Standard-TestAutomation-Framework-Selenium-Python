from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities


class ResourceContextControls:

    def __init__(self, driver):
        self.driver = driver

    context_dropdown = (By.XPATH, "//span[@aria-owns = 'nav-context-list_listbox']")
    resource_context = (By.XPATH, "//ul[@id = 'nav-context-list_listbox']//li[contains(text(),'Resources')]")
    report_group = (By.XPATH, "//span[@aria-owns='nav-report-group-list_listbox']")
    arpr_reports = (By.XPATH, "//ul[@id='nav-report-group-list_listbox']//li[contains(text(),'ARPR Reports')]")
    sum_reports = (By.XPATH, "//li[contains(text(),'SUM Reports')]")
    report_dropdown = (By.XPATH, "//div[@id = 'nav_report_list_chosen']")
    hierarchy_dropdown = (By.XPATH, "//span[@aria-owns = 'nav-hierarchy-list_listbox']")
    aoO_LoB_Field = (By.XPATH, "//li[contains(text(),'06.	 Asset Hierarchy (AoO - LoB - Field)')]")
    version = (By.XPATH,"//div[@id = 'nav_version_list_chosen']")
    arpr_Version = (By.XPATH,"//li[contains(text(),'2024 ARPR Ledger')]")
    filter = (By.XPATH,"//div[@id = 'nav_filter_list_chosen']")
    no_filter = (By.XPATH,"//ul[@class = 'chosen-results']//li[contains(text(),'< No Filter >')]")
    report_header =(By.XPATH, "//li[@id = 'group-report']")
    report_viewer = (By.XPATH,"//li[contains(text(),'Report Viewer')]")
    report_option = (By.XPATH,"//li[contains(text(),'Report Options')]")
    node = (By.XPATH,"//a[@title = 'AoO Name: Ayushi Test AoO']")
    
    def Context_dropdown(self):
        return self.driver.find_element(*ResourceContextControls.context_dropdown)
    def Resource_context(self):
        return self.driver.find_element(*ResourceContextControls.resource_context)
    def Report_group(self):
        return self.driver.find_element(*ResourceContextControls.report_group)
    def ARPR_reports(self):
        return self.driver.find_element(*ResourceContextControls.arpr_reports)
    def SUM_reports(self):
        return self.driver.find_element(*ResourceContextControls.sum_reports)
    def Report_dropdown(self):
        return self.driver.find_element(*ResourceContextControls.report_dropdown)
    def Hierarchy_dropdown(self):
        return self.driver.find_element(*ResourceContextControls.hierarchy_dropdown)
    def AoO_LoB_Field(self):
        return self.driver.find_element(*ResourceContextControls.aoO_LoB_Field)
    def Version(self):
        return self.driver.find_element(*ResourceContextControls.version)
    def ARPR_version(self):
        return self.driver.find_element(*ResourceContextControls.arpr_Version)
    def Filter(self):
        return self.driver.find_element(*ResourceContextControls.filter)
    def No_filter(self):
        return self.driver.find_element(*ResourceContextControls.no_filter)
    def Report_header(self):
        return self.driver.find_element(*ResourceContextControls.report_header)
    def Report_viewer(self):
        return self.driver.find_element(*ResourceContextControls.report_viewer)
    def Report_option(self):
        return self.driver.find_element(*ResourceContextControls.report_option)
    def Node(self):
        return self.driver.find_element(*ResourceContextControls.node)

    

#R06 Reports

    r06_01_SECP_Reserves_report = (By.XPATH, "//li[contains(text(),'R06.01 SEC Reserves')]")
    r06_02_2P_Reserves_report = (By. XPATH, "//li[contains(text(),'R06.02 2P Reserves')]")
    r06_03_3P_Reserves_report = (By.XPATH, "//li[contains(text(),'R06.03 3P Reserves')]")
    r06_04_2C_Reserves_report = (By.XPATH, "//li[contains(text(),'R06.04 2C Resources')]")
    r06_05_2U_Reserves_report = (By.XPATH, "//li[contains(text(),'R06.05 2U Resources')]")
    

    def R06_01_SECP_Reserves_report(self):
        return self.driver.find_element(*ResourceContextControls.r06_01_SECP_Reserves_report)
    def R06_02_2P_Reserves_report(self):
        return self.driver.find_element(*ResourceContextControls.r06_02_2P_Reserves_report)
    def R06_03_3P_Reserves_report(self):
        return self.driver.find_element(*ResourceContextControls.r06_03_3P_Reserves_report)
    def R06_04_2C_Reserves_report(self):
        return self.driver.find_element(*ResourceContextControls.r06_04_2C_Reserves_report)
    def R06_05_2U_Reserves_report(self):
        return self.driver.find_element(*ResourceContextControls.r06_05_2U_Reserves_report)
    
       
    #Report Options


    subtotalling_selected = (By.XPATH, "//input[@id = 'vtoc-CheckBox-Subtotal_Checkboxes-0']")
    subtotalling_Attributes = (By.XPATH, "//input[@id = 'vtoc-CheckBox-Subtotal_Checkboxes-1']")
    subtotalling_objects = (By.XPATH, "//input[@id = 'vtoc-CheckBox-Subtotal_Checkboxes-2']")
    

    def Subtotalling_selected(self):
        return self.driver.find_element(*ResourceContextControls.subtotalling_selected)
    def Subtotalling_Attributes(self):
        return self.driver.find_element(*ResourceContextControls.subtotalling_Attributes)
    def Subtotalling_objects(self):
        return self.driver.find_element(*ResourceContextControls.subtotalling_objects)


#R01 Reports

    r01_08_SUMANREV_liquids = (By.XPATH, "//li[contains(text(),'R01.08 SUMANREV Liquids')]")
    r01_09_SUMANREV_Gas = (By.XPATH, "//li[contains(text(),'R01.09 SUMANREV Gas')]")
    r01_10_SUMANREV_BOE = (By.XPATH, "//li[contains(text(),'R01.10 SUMANREV BOE')]")
    r01_11_SUMANREV_indicators = (By.XPATH, "//li[contains(text(),'R01.11 SUMANREV - Indicators')]")
    r01_12_SUMANREV_indicators_liquids = (By.XPATH, "//li[contains(text(),'R01.12 SUMANREV - Indicators Liquid')]")
    r01_13_SUMANREV_indicators_Gas = (By.XPATH, "//li[contains(text(),'R01.13 SUMANREV - Indicators Gas')]")
    r01_14_SUMANREV_indicators_BOE = (By.XPATH, "//li[contains(text(),'R01.14 SUMANREV - Indicators BOE')]")


    def R01_08_SUMANREV_Liquids(self):
        return self.driver.find_element(*ResourceContextControls.r01_08_SUMANREV_liquids)
    def R01_09_SUMANREV_Gas(self):
        return self.driver.find_element(*ResourceContextControls.r01_09_SUMANREV_Gas)
    def R01_10_SUMANREV_BOE(self):
        return self.driver.find_element(*ResourceContextControls.r01_10_SUMANREV_BOE)
    def R01_11_SUMANREV_Indicators(self):
        return self.driver.find_element(*ResourceContextControls.r01_11_SUMANREV_indicators)
    def R01_12_SUMANREV_indicators_Liquids(self):
        return self.driver.find_element(*ResourceContextControls.r01_12_SUMANREV_indicators_liquids)
    def R01_13_SUMANREV_indicators_Gas(self):
        return self.driver.find_element(*ResourceContextControls.r01_13_SUMANREV_indicators_Gas)
    def R01_14_SUMANREV_indicators_BOE(self):
        return self.driver.find_element(*ResourceContextControls.r01_14_SUMANREV_indicators_BOE)

   
    #report options

    
    units_1column = (By.XPATH, "//select[@id = 'unitSystemControl-Units-1']")
    units_2column = (By.XPATH, "//select[@id = 'unitSystemControl-Units-2']")


    def Units_1column(self):
        return self.driver.find_element(*ResourceContextControls.units_1column)
    def Units_2column(self):
        return self.driver.find_element(*ResourceContextControls.units_2column)