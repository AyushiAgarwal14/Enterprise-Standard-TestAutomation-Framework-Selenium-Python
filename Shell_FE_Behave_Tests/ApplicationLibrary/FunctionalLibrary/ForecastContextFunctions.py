import time

from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.ForecastContextControls import ForecastContextControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.AccessibilityUtilities import AccessibilityUtilities
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities
from selenium.webdriver.common.by import By

class F1:

    def __init__(self):
        self.Test_Control = ForecastContextControls(SeleniumBase.driver)

    def access_Rs1(self):
        BrowserUtilities.navigate_to_url(SeleniumBase.url)
        BrowserUtilities.maximize_window()
        #BrowserUtilities.resize_browser(1920, 1080)
        BrowserUtilities.refresh_page()

    def click_context_dropdown(self):
        time.sleep(30)
        SeleniumUtilities.click_element(self.Test_Control.Context_dropdown())
    def click_forecast_context(self):
        SeleniumUtilities.click_element(self.Test_Control.Forecast_context())
        time.sleep(2)
    def click_Report_group(self):
        SeleniumUtilities.click_element(self.Test_Control.Report_group())
        time.sleep(2)
    def click_ARPR_reports(self):
        SeleniumUtilities.click_element(self.Test_Control.ARPR_reports())
        time.sleep(2)
    def click_PUD_reports(self):
        SeleniumUtilities.click_element(self.Test_Control.PUD_reports())
        time.sleep(2)
    def click_Admin_reports(self):
        SeleniumUtilities.click_element(self.Test_Control.Admin_reports())
        time.sleep(2)
    def click_All_reports(self):
        SeleniumUtilities.click_element(self.Test_Control.All_reports())
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
    def highlight_tag_name(self):
        SeleniumUtilities.highlight_field(self.Test_Control.Highlight_tag())
        time.sleep(5)
    def highlight_h2_tag(self):
        SeleniumUtilities.highlight_field(self.Test_Control.H2_tag())
        time.sleep(5)
    def click_job_scheduler(self):
        SeleniumUtilities.click_element(self.Test_Control.Job_scheduler())
        BrowserUtilities.switch_to_child_window() 
        WaitUtilities.wait_for_element_to_be_present((By.XPATH,"//div[@class='ui-grid-row ng-scope'][1]//div[@class='ui-grid-cell-contents ng-binding ng-scope'][contains(text(),'Succeeded')]"),timeout=90)
        time.sleep(5)
    def highlight_success_message(self):
        SeleniumUtilities.highlight_field(self.Test_Control.Succeeded_message())
        # value1='Succeeded' or 'Succeeded With Warnings'
        value2=SeleniumUtilities.get_text(self.Test_Control.Succeeded_message())
        # AssertionUtilities.assert_equals(value1,value2)
        values=['Succeeded','SucceededWithWarnings','SucceededWithErrors']
        AssertionUtilities.assert_contains(value2,values)
        time.sleep(10)
     
    


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


    #PUD Approval #PUDDevelopmentYear #PUD5objectives #pudgreaterthan5BirthYear

    def click_PUDApproval_Report(self):
        SeleniumUtilities.click_element(self.Test_Control.PUDApproval_Report())
        time.sleep(2)
    def click_PUDDevelopmentYear_Report(self):
        SeleniumUtilities.click_element(self.Test_Control.PUDDevelopmentYear_Report())
        time.sleep(2)
    def click_PUD5Objectives_Report(self):
        SeleniumUtilities.click_element(self.Test_Control.PUD5Objectives_Report())
        time.sleep(2)
    def click_PUDGreaterThan5_Report(self):
        SeleniumUtilities.click_element(self.Test_Control.PUDGreaterThan5_Report())
        time.sleep(2)
    def click_PUDGreaterthan5BirthYear_Report(self):
        SeleniumUtilities.click_element(self.Test_Control.PUDGreaterthan5BirthYear_Report())
        time.sleep(2)
    def click_PUDGreaterthan5BirthYear_Report(self):
        SeleniumUtilities.click_element(self.Test_Control.PUDGreaterthan5BirthYear_Report())
        time.sleep(2)
    def click_ThroughPUD_report(self):
        SeleniumUtilities.click_element(self.Test_Control.ThroughPUD_report())
        time.sleep(2)
    def click_ActualPUD5_report(self):
        SeleniumUtilities.click_element(self.Test_Control.ActualPUD5_report())
        time.sleep(2)
    def click_ActualPUD5CYPUDcheck_report(self):
        SeleniumUtilities.click_element(self.Test_Control.ActualPUD5CYPUDcheck_report())
        time.sleep(2)




    def click_Include_objective(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Include_objective())
        time.sleep(2)
    def click_Subtotal(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Subtotal_LOB())
        time.sleep(2)
    def click_Product_group_selection(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Product_group_selection_BOE())
        time.sleep(2)
    def click_Approval_State(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Approval_State_Approved(), 'Approved')
        time.sleep(2)
    def click_Streams(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Streams_Both())
        time.sleep(2)
    def click_Output_Type(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Output_type_singlepage(), 'Single Page')
        time.sleep(2)
    def click_Include_footer(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Include_footer_Yes())
        time.sleep(2)
    def click_Report_Objectives_with_Non_Res_Dev_SubClass(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Report_Objectives_with_Non_Res_Dev_SubClass_Yes(), 'Yes')
        time.sleep(2)
    def click_Split_by_SubClass(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Split_by_SubClass_Yes(), 'Yes')
        time.sleep(2)


    
    
    #Restore to opening balance report


    def click_Restore_to_opening_balance_report(self):
        SeleniumUtilities.click_element(self.Test_Control.Restore_to_opening_balance_report())
        time.sleep(2)

    def click_Output_type_Singlepage(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Output_type(), 'Single Page')
        time.sleep(2)
    def click_Output_type_Multiplepages(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Output_type(), 'Multiple Pages')
        time.sleep(2)



    #System security filter detail Report


    def click_System_security_filter_detail(self):
        SeleniumUtilities.click_element(self.Test_Control.System_security_filter_detail())
        time.sleep(2)
    def click_Security_roles_check_report(self):
        SeleniumUtilities.click_element(self.Test_Control.Security_roles_check_report())
        time.sleep(2)


    def click_Report_type_option1(self):
        SeleniumUtilities.select_radiobutton(self.Test_Control.Report_type_option1())
        time.sleep(2)
    def click_Report_type_option2(self):
        SeleniumUtilities.select_radiobutton(self.Test_Control.Report_type_option2())
        time.sleep(2)
    def click_Report_type_option3(self):
        SeleniumUtilities.select_radiobutton(self.Test_Control.Report_type_option3())
        time.sleep(2)
    def click_Report_type_option4(self):
        SeleniumUtilities.select_radiobutton(self.Test_Control.Report_type_option4())
        time.sleep(2)



    def click_Groupby_Roles_users_roles(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Groupby_Roles_users(), 'Roles')
        time.sleep(2)
    def click_Groupby_Roles_users_users(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Groupby_Roles_users(), 'Users')
        time.sleep(2)
    def click_Include_users_not_mapped_to_security_roles(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Include_users_not_mapped_to_security_roles())
        time.sleep(2)
    def click_List_of_users_notin_security_roles_CRFP(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.List_of_users_notin_security_roles_CRFP())
        time.sleep(2)
    def click_List_of_users_notin_security_roles_SuperUSER(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.List_of_users_notin_security_roles_SuperUSER())
        time.sleep(2)
    def click_List_of_users_notin_security_roles_TA2(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.List_of_users_notin_security_roles_TA2())
        time.sleep(2)
    def click_Include_disabled_users(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Include_disabled_users())
        time.sleep(2)
    
    
    #OSA - Objective ADD


    def click_Data(self):
        SeleniumUtilities.click_element(self.Test_Control.Data())
        time.sleep(2)
    def click_Quick_Actions(self):
        SeleniumUtilities.click_element(self.Test_Control.Quick_Actions())
        time.sleep(2)
    def click_Objective_node(self):
        SeleniumUtilities.click_element(self.Test_Control.Objective_node())
        time.sleep(2)
    def click_Group_actions(self):
        SeleniumUtilities.click_element(self.Test_Control.Group_actions())
        time.sleep(2)
    def click_Objective_Actions(self):
        SeleniumUtilities.click_element(self.Test_Control.Objective_Actions())
        time.sleep(2)
    def click_Action(self):
        SeleniumUtilities.click_element(self.Test_Control.Action())
        time.sleep(2)
    def click_Objective_add(self):
        SeleniumUtilities.click_element(self.Test_Control.Objective_add())
        time.sleep(2)
    def click_Objective_name_textbox_cleartext(self):
        SeleniumUtilities.clear_text(self.Test_Control.Objective_name_textbox())
        time.sleep(2)
    def click_Objective_name_textbox(self):
        SeleniumUtilities.send_text(self.Test_Control.Objective_name_textbox(), 'Obj-A2')
        time.sleep(2)
    def click_Objective_type_Standard(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Objective_type(), 'Standard')
        time.sleep(2)
    def click_Objective_type_MakeUpOverliftUnderlift(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Objective_type(), 'Make-Up/Overlift/Underlift')
        time.sleep(2)
    def click_Objective_type_ORRI(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Objective_type(), 'ORRI')
        time.sleep(2)

    def click_Reason_for_change_Newpurchase(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Reason_for_change(), 'New Purchase')
        time.sleep(2)
    def click_Reason_for_change_Revision(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Reason_for_change(), 'Revision')
        time.sleep(2)
    def click_Reason_for_change_NewEntry(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Reason_for_change(), 'New Entry')
        time.sleep(2)
    


    def click_Resource_class_PR(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_class(), 'Prospective Resources')
        time.sleep(2)
    def click_Resource_class_CR(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_class(), 'Contingent Resources')
        time.sleep(2)
    def click_Resource_class_reserves(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_class(), 'Reserves')
        time.sleep(2)



    def click_Resource_sub_class_Play(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Play')
        time.sleep(2)
    def click_Resource_sub_class_Lead(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Lead')
        time.sleep(2)
    def click_Resource_sub_class_Prospect(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Prospect')
        time.sleep(2)
    def click_Resource_sub_class_PostLicence_PR(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Post Licence (PR)')
        time.sleep(2)


    def click_Resource_sub_class_PL(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Post Licence')
        time.sleep(2)
    def click_Resource_sub_class_NV(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Dev Not Viable')
        time.sleep(2)
    def click_Resource_sub_class_OH(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Dev On Hold')
        time.sleep(2)
    def click_Resource_sub_class_UC(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Dev Unclarified')
        time.sleep(2)
    def click_Resource_sub_class_PreDG1(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'DP Pre-DG1')
        time.sleep(2)
    def click_Resource_sub_class_PDG1(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'DP Post-DG1')
        time.sleep(2)
    def click_Resource_sub_class_PDG2(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'DP Post-DG2')
        time.sleep(2)
    def click_Resource_sub_class_PDG3(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'DP Post-DG3')
        time.sleep(2)

    def click_Resource_sub_class_Undev(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Undeveloped')
        time.sleep(2)
    def click_Resource_sub_class_Dev(self):
        SeleniumUtilities.select_from_dropdown_using_visible_text(self.Test_Control.Resource_sub_class(), 'Developed')
        time.sleep(2)


    def click_Included_in_ARPR_Yes(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Included_in_ARPR())
        time.sleep(2)
    def click_Included_in_ARPR_NO(self):
        SeleniumUtilities.unselect_checkbox(self.Test_Control.Included_in_ARPR())
        time.sleep(2)
    def click_Keep_zero_objective_NO(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Keep_zero_objective())
        time.sleep(2)
    def click_Keep_zero_objective_Yes(self):
        SeleniumUtilities.unselect_checkbox(self.Test_Control.Keep_zero_objective())
        time.sleep(2)
    def click_Add_zero_lowYAP_forecast_NO(self):
        SeleniumUtilities.select_checkbox(self.Test_Control.Add_zero_lowYAP_forecast())
        time.sleep(2)
    def click_Add_zero_lowYAP_forecast_Yes(self):
        SeleniumUtilities.unselect_checkbox(self.Test_Control.Add_zero_lowYAP_forecast())
        time.sleep(2)
    
    def click_Add_button(self):
        SeleniumUtilities.click_element(self.Test_Control.Add_button())
        time.sleep(2)

    


    






