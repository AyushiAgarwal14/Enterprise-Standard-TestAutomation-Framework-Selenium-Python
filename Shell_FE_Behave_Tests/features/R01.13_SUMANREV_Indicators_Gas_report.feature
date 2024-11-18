@web @R01.13_SUMANREV_Indicators_Gas_report
Feature: R01.13_SUMANREV_Indicators_Gas Report
    Scenario: open Rs1 and run the R01.13_SUMANREV_Indicators_Gas report
        Given user opens the rs1 application and runs the R01.13_SUMANREV_Indicators_Gas Report
        When user selects resource context and select R01.13_SUMANREV_Indicators_Gas Report
        And user selects the desired report options in R01.13_SUMANREV_Indicators_Gas Report
        Then user clicks the report viewer and generates the report in R01.13_SUMANREV_Indicators_Gas Report