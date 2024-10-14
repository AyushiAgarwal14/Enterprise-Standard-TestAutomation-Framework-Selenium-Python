@web @contractReport
Feature: Contract Report
    Scenario: open Rs1 and run the Contract report
        Given user opens the rs1 application and runs the contract Report
        When user selects resource context and select Contract Report
        And user selects the desired report options
        Then user clicks the report viewer and generates the report
