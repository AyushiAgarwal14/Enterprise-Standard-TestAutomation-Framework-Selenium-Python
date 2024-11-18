@web @ActualPUD5+Report
Feature: ActualPUD5+Report
    Scenario: open Rs1 and run the ActualPUD5+ report
        Given user opens the rs1 application and runs the ActualPUD5+ Report
        When user selects resource context and select ActualPUD5+ Report
        And user selects the desired report options in ActualPUD5+ Report
        Then user clicks the report viewer and generates the report in ActualPUD5+ Report
