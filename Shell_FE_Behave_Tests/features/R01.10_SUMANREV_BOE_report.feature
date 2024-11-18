@web @R01.10_SUMANREV_BOE_report
Feature: R01.10_SUMANREV_BOE Report
    Scenario: open Rs1 and run the R01.10_SUMANREV_BOE report
        Given user opens the rs1 application and runs the R01.10_SUMANREV_BOE Report
        When user selects resource context and select R01.10_SUMANREV_BOE Report
        And user selects the desired report options in R01.10_SUMANREV_BOE Report
        Then user clicks the report viewer and generates the report in R01.10_SUMANREV_BOE Report