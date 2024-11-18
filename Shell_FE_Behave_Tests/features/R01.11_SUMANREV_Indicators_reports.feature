@web @R01.11_SUMANREV_Indicators_reports
Feature: R01.11_SUMANREV_Indicators Report
    Scenario: open Rs1 and run the R01.11_SUMANREV_Indicators report
        Given user opens the rs1 application and runs the R01.11_SUMANREV_Indicators Report
        When user selects resource context and select R01.11_SUMANREV_Indicators Report
        And user selects the desired report options in R01.11_SUMANREV_Indicators Report
        Then user clicks the report viewer and generates the report in R01.11_SUMANREV_Indicators Report