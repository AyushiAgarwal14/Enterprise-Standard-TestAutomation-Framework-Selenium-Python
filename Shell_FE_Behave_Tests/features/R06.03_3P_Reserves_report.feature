@web @R06.03_3P_ReservesReport
Feature: R06.03_3P_Reserves Report
    Scenario: open Rs1 and run the R06.03_3P_Reserves report
        Given user opens the rs1 application and runs the R06.03_3P_Reserves Report
        When user selects resource context and select R06.03_3P_Reserves Report
        And user selects the desired report options in R06.03_3P_Reserves Report
        Then user clicks the report viewer and generates the report in R06.03_3P_Reserves Report
