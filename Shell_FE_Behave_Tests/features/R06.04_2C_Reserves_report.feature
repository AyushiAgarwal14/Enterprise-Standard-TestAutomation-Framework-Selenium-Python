@web @R06.04_2C_Reserves_Report
Feature: R06.04_2C_Reserves Report
    Scenario: open Rs1 and run the R06.04_2C_Reserves report
        Given user opens the rs1 application and runs the R06.04_2C_Reserves Report
        When user selects resource context and select R06.04_2C_Reserves Report
        And user selects the desired report options in R06.04_2C_Reserves Report
        Then user clicks the report viewer and generates the report in R06.04_2C_Reserves Report
