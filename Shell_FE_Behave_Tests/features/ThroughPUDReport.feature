@web @ThroughPUDReport
Feature: ThroughPUD Report
    Scenario: open Rs1 and run the ThroughPUD report
        Given user opens the rs1 application and runs the ThroughPUD Report
        When user selects resource context and select ThroughPUD Report
        And user selects the desired report options in ThroughPUD Report
        Then user clicks the report viewer and generates the report in ThroughPUD Report
