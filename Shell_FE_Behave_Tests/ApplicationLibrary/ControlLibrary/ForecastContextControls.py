from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities


class ForecastContextControls:

    def __init__(self, driver):
        self.driver = driver

    context_dropdown = (By.XPATH, "//span[@aria-owns = 'nav-context-list_listbox']")
    forecast_context = (By.XPATH, "//ul[@id = 'nav-context-list_listbox']//li[contains(text(),'Forecast')]")
    report_group = (By.XPATH, "//span[@aria-owns='nav-report-group-list_listbox']")
    arpr_reports = (By.XPATH, "//ul[@id='nav-report-group-list_listbox']//li[contains(text(),'ARPR Reports')]")
    pud_reports = (By.XPATH, "//li[contains(text(),'PUD Reports')]")
    admin_reports = (By.XPATH, "//li[contains(text(),'Admin Reports')]")
    all_reports = (By.XPATH, "//li[contains(text(),'< All Reports >')]")
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
    highlight_tag=(By.XPATH,"//h1")
    h2_tag=(By.XPATH,"//tr[@class='pg0 headerText']//h2")
    job_scheduler=(By.XPATH,"//div[@title='Jobs']")
    succeeded_message=(By.XPATH,"//div[@class='ui-grid-row ng-scope'][1]//div[@class='ui-grid-cell-contents ng-binding ng-scope'][contains(text(),'Succeeded')]")
    include_details_aao=(By.XPATH,"//input[@id='vtoc-CheckBox-IncludeDetailsRpt1-0']")
    
    
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
    def All_reports(self):
        return self.driver.find_element(*ForecastContextControls.all_reports)
    def Admin_reports(self):
        return self.driver.find_element(*ForecastContextControls.admin_reports)
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
    def Highlight_tag(self):
        return self.driver.find_element(*ForecastContextControls.highlight_tag)
    def H2_tag(self):
        return self.driver.find_element(*ForecastContextControls.h2_tag)
    def Job_scheduler(self):
        return self.driver.find_element(*ForecastContextControls.job_scheduler)
    def Succeeded_message(self):
        return self.driver.find_element(*ForecastContextControls.succeeded_message)
    



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


#PUDApproval #PUDDevelopmentYear #PUD5Objectives #PUDGreaterthan5 #PUDGreaterthan5BirthYear #ThroughPUD
    
    pudapproval_report = (By.XPATH, "//li[contains(text(),'PUD Approval')]")
    puddevelopmentyear_report = (By.XPATH, "//li[contains(text(),'PUD Development Year')]")
    pud5Objectives_report = (By.XPATH, "//li[contains(text(),'PUD5+ Objectives')]")
    pudgreaterthan5_report = (By.XPATH, "//li[@data-option-array-index = '45']")
    pudgreaterthan5BirthYear_report = (By.XPATH, "//li[contains(text(),'PUD Greater Than 5 Birth Year')]")
    throughPUD_report = (By.XPATH, "//li[contains(text(),'Through PUD')]")
    actualPUD5_report = (By.XPATH, "//li[@data-option-array-index = '13']")
    actualPUD5CYPUDcheck_report = (By.XPATH, "//li[contains(text(),'Actual PUD5+ CY PUD Check')]")


    
    def PUDApproval_Report(self):
        return self.driver.find_element(*ForecastContextControls.pudapproval_report)
    def PUDDevelopmentYear_Report(self):
        return self.driver.find_element(*ForecastContextControls.puddevelopmentyear_report)
    def PUDGreaterThan5_Report(self):
        return self.driver.find_element(*ForecastContextControls.pudgreaterthan5_report)
    def PUD5Objectives_Report(self):
        return self.driver.find_element(*ForecastContextControls.pud5Objectives_report)
    def PUDGreaterthan5BirthYear_Report(self):
        return self.driver.find_element(*ForecastContextControls.pudgreaterthan5BirthYear_report)
    def ThroughPUD_report(self):
        return self.driver.find_element(*ForecastContextControls.throughPUD_report)
    def ActualPUD5_report(self):
        return self.driver.find_element(*ForecastContextControls.actualPUD5_report)
    def ActualPUD5CYPUDcheck_report(self):
        return self.driver.find_element(*ForecastContextControls.actualPUD5CYPUDcheck_report)
    


     #Report options



    include_objective = (By.XPATH, "//input[@name = 'vtoc-CheckBox-Include_Objectives']")
    subtotal_LOB = (By.XPATH, "//input[@value = 'LOB']")
    product_group_selection_BOE = (By.XPATH, "//input[@value = 'BOE']")
    approval_State_approved = (By.XPATH, "//select[@id = 'vtoc-DropDown-ApprovalState-listbox']")
    streams_Both = (By.XPATH, "//input[@value = 'BOTH']")
    output_type_singlepage = (By.XPATH, "//select[@id = 'vtoc-DropDown-OutputType-listbox']")
    include_footer_Yes = (By.XPATH, "//input[@value = 'YES']")
    report_objectives_with_Non_Res_Dev_SubClass_Yes = (By.XPATH, "//select[@id ='vtoc-DropDown-IncludeNonResDev-listbox']")
    split_by_subClass_Yes = (By.XPATH, "//select[@id ='vtoc-DropDown-SplitBySubClass-listbox']")



   
    def Include_objective(self):
        return self.driver.find_element(*ForecastContextControls.include_objective)
    def Subtotal_LOB(self):
        return self.driver.find_element(*ForecastContextControls.subtotal_LOB)
    def Product_group_selection_BOE(self):
        return self.driver.find_element(*ForecastContextControls.product_group_selection_BOE)
    def Approval_State_Approved(self):
        return self.driver.find_element(*ForecastContextControls.approval_State_approved)
    def Streams_Both(self):
        return self.driver.find_element(*ForecastContextControls.streams_Both)
    def Output_type_singlepage(self):
        return self.driver.find_element(*ForecastContextControls.output_type_singlepage)
    def Include_footer_Yes(self):
        return self.driver.find_element(*ForecastContextControls.include_footer_Yes)
    def Report_Objectives_with_Non_Res_Dev_SubClass_Yes(self):
        return self.driver.find_element(*ForecastContextControls.report_objectives_with_Non_Res_Dev_SubClass_Yes)
    def Split_by_SubClass_Yes(self):
        return self.driver.find_element(*ForecastContextControls.split_by_subClass_Yes)



#Restore to opening balance report


    restore_to_opening_balance_report = (By.XPATH, "//li[contains(text(),'Restore to Opening Balance Report')]")
    
    def Restore_to_opening_balance_report(self):
        return self.driver.find_element(*ForecastContextControls.restore_to_opening_balance_report)
    
    output_type = (By.XPATH, "//select[@id = 'vtoc-DropDown-OutputType-listbox']")


    def Output_type(self):
        return self.driver.find_element(*ForecastContextControls.output_type)
    


#System security filter detail Report     #Security roles check report

    system_security_filter_detail = (By.XPATH, "//li[contains(text(),'System Security Filter Detail Report')]")
    security_roles_check_report = (By.XPATH, "//li[contains(text(),'Security - Roles Check')]")


    def System_security_filter_detail(self):
        return self.driver.find_element(*ForecastContextControls.system_security_filter_detail)
    def Security_roles_check_report(self):
        return self.driver.find_element(*ForecastContextControls.security_roles_check_report)
    

    report_type_option1 = (By.XPATH, "//input[@id = 'vtoc-RadioStacked-system_security_filter_selections-0']")
    report_type_option2 = (By.XPATH, "//input[@id = 'vtoc-RadioStacked-system_security_filter_selections-1']")
    report_type_option3 = (By.XPATH, "//input[@id = 'vtoc-RadioStacked-system_security_filter_selections-2']")
    report_type_option4 = (By.XPATH, "//input[@id = 'vtoc-RadioStacked-system_security_filter_selections-3']")
    groupby_Roles_users = (By.XPATH, "//select[@id = 'vtoc-DropDown-Group_Roles_Users-listbox']")
    include_users_not_mapped_to_security_roles = (By.XPATH, "//input[@id = 'vtoc-CheckBox-IncludeNonRoleMappedUsers-0']")
    list_of_users_notin_security_roles_CRFP = (By.XPATH, "//input[@id = 'vtoc-CheckBoxStacked-ShowUsersNotInRole-1']")
    list_of_users_notin_security_roles_SuperUSER = (By.XPATH, "//input[@id = 'vtoc-CheckBoxStacked-ShowUsersNotInRole-71']")
    list_of_users_notin_security_roles_TA2 = (By.XPATH, "//input[@id = 'vtoc-CheckBoxStacked-ShowUsersNotInRole-73']")
    include_disabled_users = (By.XPATH, "//input[@id = 'vtoc-CheckBox-IncludeDisabledUsers-0']")

    
    
    def Report_type_option1(self):
        return self.driver.find_element(*ForecastContextControls.report_type_option1)
    def Report_type_option2(self):
        return self.driver.find_element(*ForecastContextControls.report_type_option2)
    def Report_type_option3(self):
        return self.driver.find_element(*ForecastContextControls.report_type_option3)
    def Report_type_option4(self):
        return self.driver.find_element(*ForecastContextControls.report_type_option4)
    
    def Groupby_Roles_users(self):
        return self.driver.find_element(*ForecastContextControls.groupby_Roles_users)
    def Include_users_not_mapped_to_security_roles(self):
        return self.driver.find_element(*ForecastContextControls.include_users_not_mapped_to_security_roles)
    def List_of_users_notin_security_roles_CRFP(self):
        return self.driver.find_element(*ForecastContextControls.list_of_users_notin_security_roles_CRFP)
    def List_of_users_notin_security_roles_SuperUSER(self):
        return self.driver.find_element(*ForecastContextControls.list_of_users_notin_security_roles_SuperUSER)
    def List_of_users_notin_security_roles_TA2(self):
        return self.driver.find_element(*ForecastContextControls.list_of_users_notin_security_roles_TA2)
    def Include_disabled_users(self):
        return self.driver.find_element(*ForecastContextControls.include_disabled_users)


#OSA - Objective ADD

    data = (By.XPATH, "//li[@id = 'group-data']")
    quick_Actions = (By.XPATH, "//li[@id = 'page-update-data']")
    objective_node = (By.XPATH, "//a[contains(text(),'A1 - CR NV')]")
    group_actions = (By.XPATH, "//div[@id = 'ddlUpdaterGroups_chosen']")
    objective_actions = (By.XPATH, "//li[contains(text(),'Objective Actions')]")
    action = (By.XPATH, "//div[@id = 'ddlUpdaters_chosen']")
    objective_add = (By.XPATH, "//li[contains(text(),'Objective Add')]")
    objective_name_textbox = (By.XPATH, "//input[@id ='textBox-OnScreen_ObJName-text']")
    objective_type = (By.XPATH, "//select[@id ='cascDropDownControl-OnScreen_AddObjDetails-ddl-0']")
    reason_for_change = (By.XPATH, "//select[@id ='cascDropDownControl-OnScreen_AddObjDetails-ddl-1']")
    resource_class  = (By.XPATH, "//select[@id ='cascDropDownControl-OnScreen_AddObjDetails-ddl-2']")
    resource_sub_class = (By.XPATH, "//select[@id ='cascDropDownControl-OnScreen_AddObjDetails-ddl-3']")
    included_in_ARPR = (By.XPATH, "//input[@id ='vtoc-CheckBox-OnScreen_IncludedInARPR-0']")
    keep_zero_objective = (By.XPATH, "//input[@id ='vtoc-CheckBox-OnScreen_KeepZeroObj-0']")
    add_zero_lowYAP_forecast = (By.XPATH, "//input[@id ='vtoc-CheckBox-OnScreen_Add_zero_low_YAP_forecast-0']")
    add_button = (By.XPATH, "//button[@data-class ='updateData.btnUpdate']")


    def Data(self):
        return self.driver.find_element(*ForecastContextControls.data)
    def Quick_Actions(self):
        return self.driver.find_element(*ForecastContextControls.quick_Actions)
    def Group_actions(self):
        return self.driver.find_element(*ForecastContextControls.group_actions)
    def Objective_Actions(self):
        return self.driver.find_element(*ForecastContextControls.objective_actions)
    def Action(self):
        return self.driver.find_element(*ForecastContextControls.action)
    def Objective_add(self):
        return self.driver.find_element(*ForecastContextControls.objective_add)
    def Objective_node(self):
        return self.driver.find_element(*ForecastContextControls.objective_node)
    def Objective_name_textbox(self):
        return self.driver.find_element(*ForecastContextControls.objective_name_textbox)
    def Objective_type(self):
        return self.driver.find_element(*ForecastContextControls.objective_type)
    def Reason_for_change(self):
        return self.driver.find_element(*ForecastContextControls.reason_for_change)
    def Resource_class(self):
        return self.driver.find_element(*ForecastContextControls.resource_class)
    def Resource_sub_class(self):
        return self.driver.find_element(*ForecastContextControls.resource_sub_class)
    def Included_in_ARPR(self):
        return self.driver.find_element(*ForecastContextControls.included_in_ARPR)
    def Keep_zero_objective(self):
        return self.driver.find_element(*ForecastContextControls.keep_zero_objective)
    def Add_zero_lowYAP_forecast(self):
        return self.driver.find_element(*ForecastContextControls.add_zero_lowYAP_forecast)
    def Add_button(self):
        return self.driver.find_element(*ForecastContextControls.add_button)
    
    




