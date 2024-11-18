@web @OSA_Objective_ADD
Feature: OSA_Objective_ADD
    Scenario: open Rs1 and perform the OSA_Objective_ADD action.
        Given user opens the rs1 application and add a new objective    
        When user selects forecast context and select objective add action under objective actions
        And user provides desired input to add a objective
        Then user clicks on ADD button and add a objective
