@web @R06.01_SECP_Reserves_report
Feature: R06.01SECReserves Report
    Scenario: open Rs1 and run the R06.01SECReserves report
        Given user opens the rs1 application and runs the R06.01SECReserves Report
        When user selects resource context and select R06.01SECReserves Report
        And user selects the desired report options in R06.01SECReserves Report
        Then user clicks the report viewer and generates the report in R06.01SECReserves Report
