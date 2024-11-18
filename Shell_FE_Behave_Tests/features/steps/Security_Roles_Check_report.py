from behave import *
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ForecastContextFunctions import F1
#from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities

@given('user opens the rs1 application and runs the Security_Roles_Check Report')
def step_impl(context):
        context.forecast_function = F1()
        context.forecast_function.access_Rs1()


@When('user selects resource context and select Security_Roles_Check Report')
def step_impl(context):
    context.forecast_function.click_context_dropdown()
    context.forecast_function.click_forecast_context()

    context.forecast_function.click_Report_group()
    context.forecast_function.click_All_reports()

    context.forecast_function.click_Report_dropdown()
    context.forecast_function.click_Security_roles_check_report()

    context.forecast_function.click_hierarchy_dropwdown()
    context.forecast_function.click_AoO_LoB_Field()

    context.forecast_function.click_version()
    context.forecast_function.click_ARPR_version()

    context.forecast_function.click_filter()
    context.forecast_function.click_No_filter()
  
    
@When('user selects the desired report options in Security_Roles_Check Report')
def step_impl(context):
      
    context.forecast_function.click_Report_option()
    context.forecast_function.click_Groupby_Roles_users_roles()
    context.forecast_function.click_Include_users_not_mapped_to_security_roles()
    context.forecast_function.click_List_of_users_notin_security_roles_CRFP()
    context.forecast_function.click_List_of_users_notin_security_roles_SuperUSER()
    context.forecast_function.click_List_of_users_notin_security_roles_TA2()
    context.forecast_function.click_Include_disabled_users()
    
    

@Then('user clicks the report viewer and generates the Security_Roles_Check report')
def step_impl(context):
     
     context.forecast_function.click_Node()
     context.forecast_function.highlight_tag_name()
     context.forecast_function.click_job_scheduler()
     context.forecast_function.highlight_success_message() 
