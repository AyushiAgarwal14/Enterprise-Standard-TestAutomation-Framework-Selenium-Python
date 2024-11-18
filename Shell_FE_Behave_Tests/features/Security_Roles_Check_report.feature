@web @Security_Roles_Check_report
Feature: Security_Roles_Check Report
    Scenario: open Rs1 and run the Security_Roles_Check report
        Given user opens the rs1 application and runs the Security_Roles_Check Report
        When user selects resource context and select Security_Roles_Check Report
        And user selects the desired report options in Security_Roles_Check Report
        Then user clicks the report viewer and generates the Security_Roles_Check report 

