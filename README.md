# QA Automation Test - Website

This repository contains the automated UI testing framework for the RSPRO website. The project is designed using the **Page Object Model (POM)** design pattern to enhance test maintenance and reduce code duplication.

## Technologies & Frameworks
* **Programming Language:** Python 3.11
* **Browser Automation:** Selenium WebDriver
* **Test Framework:** Pytest
* **Data-Driven Testing:** JSON & Excel files (handled via custom utilities) , etc
* **URL:** https://pro.repairsolutions.com/

## Detailed Project Structure
```
qa-automation-test-rspro-website/
├── .idea/
├── .pytest_cache/
├── .venv/
├── allure-results/
├── assets/
├── base_pages/
│   ├── __pycache__/
│   ├── pages/
│   │   ├── __pycache__/
│   │   ├── Auth_Pages/
│   │   ├── HomePage_Pages/
│   │   ├── My_Report_Pages/                          -----> Example : Location containing the My Report Page Objects category
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   └── My_Report_page.py                     -----> Example : single page
│   │   ├── Products_Pages/
│   │   ├── Support_Pages/
│   │   ├── Technical_Center_Pages/
│   │   ├── __init__.py
│   │   └── base_page.py                              -----> Inherited from here
│   └── __init__.py
├── configurations/
│   └── config.ini
├── logs/
├── reports/
├── screenshots/
├── test_cases/
│   ├── __pycache__/
│   └── tests/
│       ├── __pycache__/
│       ├── Auth_Tests/
│       ├── HomePage_Tests/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── Introduction_Features_test.py
│       ├── My_Report_Tests/                         -----> Example : Location of Test Scripts for My Report section
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── My_Report_test.py                    -----> Example : Test scripts
│       ├── Products_Tests/
│       ├── Support_Tests/
│       ├── Technical_Center_Tests/
│       ├── __init__.py
│       └── conftest.py
├── test_data/
│   ├── emerging_technologies_data/
│   ├── dtc_library.json
│   ├── login.json
│   ├── my_reports.json
│   ├── sign_up_invalid_email.json
│   └── zipcode_usa_canada.xlsx
├── utilities/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── custom_logger.py
│   ├── json_reader.py
│   ├── read_properties.py                         -----> Utility to read and fetch data from configuration files.
│   ├── sign_up_excel.py
│   └── waitHelper.py                              -----> Contains the custom waits function       
├── .gitlab-ci.yml
├── checkpoint_index.txt
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
├── runner.dockerfile
└── sign_up_zipcode_result.csv
```
This framework strictly follows the **Page Object Model (POM)** pattern. The project is modularized by feature to ensure scalability and easy maintenance.

* **`base_pages/`**: Contains the Page Object classes that represent the web UI.

  * `base_page.py`: The foundational parent class. It contains common wrapper methods for Selenium WebDriver actions (e.g., custom clicks, sending keys, explicit waits) that all other page classes inherit.

* **`configurations/`**: Contains environment configurations, such as base URLs, browser specific settings, markers for each test class, environment variables.

* **`logs/`**: 
  * `.log`: The central log file. It records step-by-step execution details, warnings, and errors during test runs for debugging purposes.

* **`reports/`**: The destination folder for generated test execution reports (e.g., Pytest-HTML or Allure reports) to review test pass/fail metrics.

* **`screenshots/`**: Automatically captures and saves screenshots of the browser state whenever a test assertion fails, aiding in quick root-cause analysis.

* **`test_cases/`**: Contains the actual Pytest execution scripts.
  * **`tests/`**: Test files organized to mirror the `base_pages` structure (e.g., `Auth_Tests`, `Technical_Center_Tests`, `My_Report_Tests`). For each module, inside that base_pages are the test classes related to that module (e.g., `Technical_Center_Tests`/`Emerging_Technologies_test.py`). This keeps tests logically separated by feature.
  * `conftest.py`: The Pytest configuration file. It contains essential fixtures such as WebDriver initialization, teardown processes, and shared resources used across multiple test files. Additionally, The Automation is currently running in headless mode, and it will expand to include more browsers for testing, such as Edge, Firefox, etc.

* **`test_data/`**: The repository for all external data used in Data-Driven Testing (DDT). Separating data from code ensures tests can be run with multiple datasets without altering the test logic.
  * `emerging_technologies_data/`: Feature-specific data folders.
  * `*.json` (e.g., `login.json`, `dtc_library.json`): JSON files storing test inputs and expected results.
  * `*.xlsx` (e.g., `zipcode_usa.xlsx`): Excel files used for testing features that require large datasets, like zipcode validation.

* **`utilities/`**: A collection of reusable helper scripts and tools that support the test framework.
  * `custom_logger.py`: Configures and generates the logging format used in `logs/RSPROwebsite.log`.
  * `json_reader.py`: Utility functions to parse and extract test data from JSON files.
  * `read_properties.py`: Utility to read and fetch data from configuration files.
  * `sign_up_excel.py`: Utility to read and iterate through data in Excel (`.xlsx`) files.
  * `waitHelper.py`: Custom explicit wait implementations to handle dynamic UI elements and synchronization issues.

* **`main.py`**: The main entry point or custom run script to execute specific test suites or administrative tasks. However, this file is currently useless.

## Getting Started
### Prerequisites
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
