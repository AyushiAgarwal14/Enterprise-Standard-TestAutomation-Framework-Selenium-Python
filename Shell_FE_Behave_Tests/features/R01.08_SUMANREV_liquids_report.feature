@web @R01.08_SUMANREV_liquids_report
Feature: R01.08_SUMANREV_liquids Report
    Scenario: open Rs1 and run the R01.08_SUMANREV_liquids report
        Given user opens the rs1 application and runs the R01.08_SUMANREV_liquids Report
        When user selects resource context and select R01.08_SUMANREV_liquids Report
        And user selects the desired report options in R01.08_SUMANREV_liquids Report
        Then user clicks the report viewer and generates the report in R01.08_SUMANREV_liquids Report