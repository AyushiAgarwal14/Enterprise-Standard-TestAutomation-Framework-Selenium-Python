@web @ActualPUD5+CYPUDcheckReport
Feature: ActualPUD5+CYPUDcheckReport
    Scenario: open Rs1 and run the ActualPUD5+CYPUDcheck report
        Given user opens the rs1 application and runs the ActualPUD5+CYPUDcheck Report
        When user selects resource context and select ActualPUD5+CYPUDcheck Report
        And user selects the desired report options in ActualPUD5+CYPUDcheck Report
        Then user clicks the report viewer and generates the report in ActualPUD5+CYPUDcheck Report
