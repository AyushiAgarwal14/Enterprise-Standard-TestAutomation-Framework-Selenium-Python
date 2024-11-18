from behave import *
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.ForecastContextFunctions import F1
#from Shell_FE_Selenium_Core.Utilities.AssertionUtilities import AssertionUtilities

@given('user opens the rs1 application and add a new objective')
def step_impl(context):
        context.forecast_function = F1()
        context.forecast_function.access_Rs1()


@When('user selects forecast context and select objective add action under objective actions')
def step_impl(context):
    context.forecast_function.click_context_dropdown()
    context.forecast_function.click_forecast_context()

    context.forecast_function.click_hierarchy_dropwdown()
    context.forecast_function.click_AoO_LoB_Field()

    context.forecast_function.click_version()
    context.forecast_function.click_ARPR_version()

    context.forecast_function.click_filter()
    context.forecast_function.click_No_filter()

    context.forecast_function.click_Objective_node()
    context.forecast_function.click_Data()
    context.forecast_function.click_Quick_Actions()
  
    
@When('user provides desired input to add a objective')
def step_impl(context):
      
    context.forecast_function.click_Group_actions()
    context.forecast_function.click_Objective_Actions()
    context.forecast_function.click_Action()
    context.forecast_function.click_Objective_add()
    context.forecast_function.click_Objective_name_textbox_cleartext()
    context.forecast_function.click_Objective_name_textbox()
    context.forecast_function.click_Objective_type_Standard()
    context.forecast_function.click_Reason_for_change_NewEntry() 
    context.forecast_function.click_Resource_class_CR()
    context.forecast_function.click_Resource_sub_class_PDG1() 
    context.forecast_function.click_Included_in_ARPR_Yes()
    context.forecast_function.click_Keep_zero_objective_NO() 
    context.forecast_function.click_Add_zero_lowYAP_forecast_NO()
    


@Then('user clicks on ADD button and add a objective')
def step_impl(context):
     
     context.forecast_function.click_Add_button()
     context.forecast_function.click_job_scheduler()
     context.forecast_function.highlight_success_message() 

     
