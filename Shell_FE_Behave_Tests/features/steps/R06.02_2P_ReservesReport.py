from behave import *
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ResourceContextFunctions import F2
#from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities

@given('user opens the rs1 application and runs the R06.02_2P_Reserves Report')
def step_impl(context):
        context.Resource_function = F2()
        context.Resource_function.access_Rs1()


@When('user selects resource context and select R06.02_2P_Reserves Report')
def step_impl(context):
    context.Resource_function.click_context_dropdown()
    context.Resource_function.click_Resource_context()

    context.Resource_function.click_Report_group()
    context.Resource_function.click_ARPR_reports()

    context.Resource_function.click_Report_dropdown()
    context.Resource_function.click_R06_02_2P_Reserves_report()

    context.Resource_function.click_hierarchy_dropwdown()
    context.Resource_function.click_AoO_LoB_Field()

    context.Resource_function.click_version()
    context.Resource_function.click_ARPR_version()

    context.Resource_function.click_filter()
    context.Resource_function.click_No_filter()
  
    
@When('user selects the desired report options in R06.02_2P_Reserves Report')
def step_impl(context):
      
    context.Resource_function.click_Report_option()
    context.Resource_function.click_Subtotalling_selected()
    context.Resource_function.click_Subtotalling_Attributes()
    context.Resource_function.click_Subtotalling_objects()
    

@Then('user clicks the report viewer and generates the report in R06.02_2P_Reserves Report')
def step_impl(context):
     
     context.Resource_function.click_Node()
     context.forecast_function.highlight_tag_name()
     context.forecast_function.click_job_scheduler()
     context.forecast_function.highlight_success_message() 