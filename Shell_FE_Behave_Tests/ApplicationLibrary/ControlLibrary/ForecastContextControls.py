from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities


class ForecastContextControls:

    def __init__(self, driver):
        self.driver = driver

    context_dropdown = (By.XPATH, "//span[@aria-owns = 'nav-context-list_listbox']")
    forecast_context = (By.XPATH, "//ul[@id = 'nav-context-list_listbox']//li[contains(text(),'Forecast')]")
    report_group = (By.XPATH, "//span[@aria-owns='nav-report-group-list_listbox']")
    arpr_reports = (By.XPATH, "//ul[@id='nav-report-group-list_listbox']//li[contains(text(),'ARPR Reports')]")
    pud_reports = 
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
        return self.driver.find_element(*ForecastContextControls.context_dropdown)
    def Forecast_context(self):
        return self.driver.find_element(*ForecastContextControls.forecast_context)
    def Report_group(self):
        return self.driver.find_element(*ForecastContextControls.report_group)
    def ARPR_reports(self):
        return self.driver.find_element(*ForecastContextControls.arpr_reports)
    def PUD_reports(self):
        return self.driver.find_element(*ForecastContextControls.pud_reports)
    def Report_dropdown(self):
        return self.driver.find_element(*ForecastContextControls.report_dropdown)
    def Hierarchy_dropdown(self):
        return self.driver.find_element(*ForecastContextControls.hierarchy_dropdown)
    def AoO_LoB_Field(self):
        return self.driver.find_element(*ForecastContextControls.aoO_LoB_Field)
    def Version(self):
        return self.driver.find_element(*ForecastContextControls.version)
    def ARPR_version(self):
        return self.driver.find_element(*ForecastContextControls.arpr_Version)
    def Filter(self):
        return self.driver.find_element(*ForecastContextControls.filter)
    def No_filter(self):
        return self.driver.find_element(*ForecastContextControls.no_filter)
    def Report_header(self):
        return self.driver.find_element(*ForecastContextControls.report_header)
    def Report_viewer(self):
        return self.driver.find_element(*ForecastContextControls.report_viewer)
    def Report_option(self):
        return self.driver.find_element(*ForecastContextControls.report_option)
    def Node(self):
        return self.driver.find_element(*ForecastContextControls.node)



#Contract Report
   
    contract_Report = (By.XPATH, "//li[contains(text(),'Contract Report')]")
    report_type_Allcontracts = (By.XPATH, "//input[@id = 'vtoc-RadioStacked-ContractReportType-0']")
    include_old_contract_details_Yes = (By.XPATH, "//input[@id = 'vtoc-CheckBox-IncludeOldContractDetails-0']")
    include_Objectives_Yes = (By.XPATH, "//input[@id = 'vtoc-CheckBox-IncludeObjLinkedtoContract-0']")
    units_1000acres = (By.XPATH, "//select[@id = 'vtoc-DropDown-Acres-listbox']")


    def Contract_Report(self):
        return self.driver.find_element(*ForecastContextControls.contract_Report)
    def Report_type_Allcontracts(self):
        return self.driver.find_element(*ForecastContextControls.report_type_Allcontracts)
    def Include_old_contract_details_Yes(self):
        return self.driver.find_element(*ForecastContextControls.include_old_contract_details_Yes)
    def Include_Objectives_Yes(self):
        return self.driver.find_element(*ForecastContextControls.include_Objectives_Yes)
    def Units_1000(self):
        return self.driver.find_element(*ForecastContextControls.units_1000acres)


#PUDApproval Report
    
    PUDApproval_report = 
    Include_objective =
    Subtotal = 
    Product_group_selection = 
    Approval_State = 
    Streams = 
    Output_Type = 
    Include_footer = 
