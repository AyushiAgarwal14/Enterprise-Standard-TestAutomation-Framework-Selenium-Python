from behave import *
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ResourceContextFunctions import F2
#from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities

@given('user opens the rs1 application and runs the R01.11_SUMANREV_Indicators Report')
def step_impl(context):
        context.Resource_function = F2()
        context.Resource_function.access_Rs1()


@When('user selects resource context and select R01.11_SUMANREV_Indicators Report')
def step_impl(context):
    context.Resource_function.click_context_dropdown()
    context.Resource_function.click_Resource_context()

    context.Resource_function.click_Report_group()
    context.Resource_function.click_SUM_reports()

    context.Resource_function.click_Report_dropdown()
    context.Resource_function.click_R01_11_SUMANREV_Indicators()

    context.Resource_function.click_hierarchy_dropwdown()
    context.Resource_function.click_AoO_LoB_Field()

    context.Resource_function.click_version()
    context.Resource_function.click_ARPR_version()

    context.Resource_function.click_filter()
    context.Resource_function.click_No_filter()
  
    
@When('user selects the desired report options in R01.11_SUMANREV_Indicators Report')
def step_impl(context):
      
    context.Resource_function.click_Report_option()
    context.Resource_function.click_Units_1column()
    context.Resource_function.click_Units_2column()
    

@Then('user clicks the report viewer and generates the report in R01.11_SUMANREV_Indicators Report')
def step_impl(context):
     
     context.Resource_function.click_Node()
     context.forecast_function.highlight_tag_name()
     context.forecast_function.click_job_scheduler()
     context.forecast_function.highlight_success_message() 
