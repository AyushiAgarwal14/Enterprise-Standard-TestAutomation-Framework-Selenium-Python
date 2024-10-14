# Enterprise Standard Test Automation Framework - Selenium Python

The Shell FE Python Automation framework is a robust framework developed by the Functional Excellence QA with the aim to provide UI, Mobile and API automation solution for the project automation needs as a single entity.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Description

This framework is written in Python and utilizes Selenium for UI automation, Appium for mobile automation, and Requests for API automation.

## Features

The framework offers a wide range of features, including:
   - DB validation
   - Accessibility testing
   - Visual testing
   - Multi-browser testing
   - Parallel execution
   - CI/CD integration of automated tests
   - Developed using a Behavior-Driven Development (BDD) approach, providing visually appealing reports for test results.

## Installation

To set up the framework on your local machine, follow the steps provided below.

1. Install Python: Install Python by following the instructions provided in the [Devkit](https://devkit.shell.com/content/tools/devrights).
2. Install PyCharm: Download PyCharm by following the instructions in the [Devkit](https://devkit.shell.com/content/tools/devrights).
3. Set up a Virtual Environment: Do not select the Virtual Environment from the initial window. Instead, follow these steps in PyCharm:
   - Open the framework in PyCharm.
   - Go to File -> Settings -> Python Interpreter.
   - Click on the 'wheel' icon and select "Add...".
   - If no virtual environment has been configured previously, select Virtualenv Environment -> New Environment (A venv folder will be mapped to the current project path in the 'Location' field).
   - Select a valid location where python.exe is present on your machine.
   - Click OK.
   - Once the virtual environment has been activated, the folder path in the terminal will be prefixed with `(venv)`.
   - [optional]Go to the Terminal in PyCharm and activate the virtual environment using the following command: `venv/scripts/activate`
   

## Usage

1. Install the required packages for the framework by executing the following command:  
    **pip install -r requirements.txt**

2. Install the Selenium Core package by executing the following command:  
    **pip install "Shell_FE_Selenium_Core" git+https://github.com/sede-x/Enterprise-Standard-TestAutomation-Framework-Selenium-Python.git@main**
   
3. If you wish to uninstall any installed Packages installed then run the below command:  
    **pip uninstall Package_Name**
   
4. If you wish to update the Selenium Core Package then run below command:  
   **pip install --upgrade Package_Name**
    

## Contribution

We welcome contributions from our organization through innersource. If you would like to contribute to the project, please follow these steps:

1. Fork the repository and create a new branch for your contribution.
2. Make your desired changes and improvements to the code.
3. Ensure that your code adheres to our coding standards and guidelines.
4. Test your changes thoroughly to ensure they do not introduce any issues.
5. Submit a pull request with the help of contributor from your branch to the main repository's branch.
6. Provide a clear and concise description of your changes in the pull request.
7. Our team will review your contribution and provide feedback or suggestions if necessary.
8. Once your contribution has been approved, it will be merged into the main repository.

We appreciate your interest in improving the project through innersource contributions. Thank you for your support!

## License

This project is Maintained by Functional Excellence QA and for any queries please do reach out to Functional Excellence QA.
