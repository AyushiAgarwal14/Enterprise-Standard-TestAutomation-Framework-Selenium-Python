@web @PUD5ObjectivesReport
Feature: PUDApproval Report
    Scenario: open Rs1 and run the PUD5+ Objectives report
        Given user opens the rs1 application and runs the PUD5+ Objectives Report
        When user selects resource context and select PUD5+ Objectives Report
        And user selects the desired report options in PUD5+ Objectives Report
        Then user clicks the report viewer and generates the report in PUD5+ Objectives Report
