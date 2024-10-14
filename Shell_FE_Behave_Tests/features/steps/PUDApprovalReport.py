from behave import *
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ForecastContextFunctions import F1
#from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities

@given('user opens the rs1 application and runs the contract Report')
def step_impl(context):
        context.forecast_function = F1()
        context.forecast_function.access_Rs1()


@When('user selects resource context and select Contract Report')
def step_impl(context):
    context.forecast_function.click_context_dropdown()
    context.forecast_function.click_forecast_context()

    context.forecast_function.click_Report_group()
    context.forecast_function.click_PUD_reports()

    context.forecast_function.click_Report_dropdown()
    context.forecast_function.click_PUDApproval_report()

    context.forecast_function.click_hierarchy_dropwdown()
    context.forecast_function.click_AoO_LoB_Field()

    context.forecast_function.click_version()
    context.forecast_function.click_ARPR_version()

    context.forecast_function.click_filter()
    context.forecast_function.click_No_filter()
  
    
@When('user selects the desired report options')
def step_impl(context):
      
    context.forecast_function.click_Report_option()
    context.forecast_function.click_Include_objective()
    context.forecast_function.click_Subtotal()
    context.forecast_function.click_Product_group_selection()
    context.forecast_function.click_Approval_State()
    context.forecast_function.click_Streams()
    context.forecast_function.click_Output_Type()
    context.forecast_function.click_Include()


@Then('user clicks the report viewer and generates the report')
def step_impl(context):
     
     context.forecast_function.click_Node()