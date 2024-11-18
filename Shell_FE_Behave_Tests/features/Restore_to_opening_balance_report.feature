@web @Restore_to_opening_balance_report
Feature: Restore_to_opening_balance Report
    Scenario: open Rs1 and run the Restore_to_opening_balance report
        Given user opens the rs1 application and runs the Restore_to_opening_balance Report
        When user selects resource context and select Restore_to_opening_balance Report
        And user selects the desired report options in Restore_to_opening_balance Report
        Then user clicks the report viewer and generates the Restore_to_opening_balance report 