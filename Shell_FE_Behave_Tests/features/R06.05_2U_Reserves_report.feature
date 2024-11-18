@web @R06.05_2U_Reserves_Report
Feature: R06.05_2U_Reserves Report
    Scenario: open Rs1 and run the R06.05_2U_Reserves report
        Given user opens the rs1 application and runs the R06.05_2U_Reserves Report
        When user selects resource context and select R06.05_2U_Reserves Report
        And user selects the desired report options in R06.05_2U_Reserves Report
        Then user clicks the report viewer and generates the report in R06.05_2U_Reserves Report
