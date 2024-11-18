@web @PUDApprovalReport
Feature: PUDApproval Report
    Scenario: open Rs1 and run the PUDApproval report
        Given user opens the rs1 application and runs the PUDApproval Report
        When user selects resource context and select PUDApproval Report
        And user selects the desired report options in PUDApproval Report
        Then user clicks the report viewer and generates the report in PUDApproval Report
