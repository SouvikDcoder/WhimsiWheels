# WhimsiWheels: A Creative Test Automation Framework

WhimsiWheels is a versatile and easy-to-use test automation framework designed for both UI and API testing. It incorporates best practices and tools to create a robust, maintainable, and scalable solution. The framework can be easily integrated into Continuous Integration pipelines and provides detailed reporting for efficient test analysis.

## Table of Contents

1.  [Getting Started](#getting-started)
2.  [Prerequisites](#prerequisites)
3.  [Installation](#installation)
4.  [Framework Structure](#framework-structure)
5.  [Usage](#usage)
6.  [Contributing](#contributing)
7.  [License](#license)
8.  [Contact](#contact)

## Getting Started

These instructions will help you set up the WhimsiWheels test automation framework on your local machine.

### Prerequisites

Ensure you have the following software installed on your system:

-   Python 3.6 or higher
-   Git
-   Docker (optional, but recommended for containerizing the test environment)

### Installation

1.  Clone the repository:


    `git clone https://github.com/your_username/WhimsiWheels.git` 

2.  Navigate to the WhimsiWheels directory:


    `cd WhimsiWheels` 

3.  Install the required Python libraries:


    `pip install -r requirements.txt` 

## Framework Structure

The WhimsiWheels framework is structured as follows:


```
WhimsiWheels/
├── config/
│   └── config.json
├── data/
│   └── testdata.json
├── pages/
│   └── home_page.py
├── performance/
│   └── locustfile.py
├── reports/
├── tests/
│   ├── api/
│   │   └── test_api_example.py
│   └── ui/
│       └── test_ui_example.py
├── utilities/
│   ├── data_factory.py
│   └── utils.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── ci/
│   ├── Jenkinsfile
│   ├── .gitlab-ci.yml
│   └── .github/
│       ├── workflows/
│       │   └── build-and-test.yml
│       └── ISSUE_TEMPLATE.md
├── requirements.txt
└── README.md 
```


The key components of the framework include:

-   **config**: Contains environment-specific settings and configuration files.
-   **data**: Contains test data, such as CSV or JSON files, to be used in test cases.
-   **pages**: Contains Page Object classes for UI testing (applicable for web applications).
-   **performance**: Contains performance and load testing scripts and related resources.
-   **reports**: Stores test execution reports, logs, and screenshots.
-   **tests**: Contains all test cases and test suites.
-   **api**: Contains API test cases and utility functions.
-   **ui**: Contains UI test cases and utility functions.
-   **utilities**: Contains utility functions, common libraries, and test data management tools.
-   **docker**: Contains Dockerfiles and related scripts for containerizing the test environment.
-   **ci**: Contains configuration files and scripts for integrating with Continuous Integration tools.
-   **requirements.txt**: Lists all the required Python libraries.
-   **README.md**: Provides documentation for the test automation framework, including setup instructions, usage guidelines, and troubleshooting information.

## Usage

To use the WhimsiWheels framework, follow these steps:

1.  Clone the repository:

	`git clone https://github.com/your_username/WhimsiWheels.git` 

2.  Navigate to the WhimsiWheels directory:

	`cd WhimsiWheels` 

3.  Install the required Python libraries:

	`pip install -r requirements.txt` 

4.  Update the `config/config.json` file with your environment-specific settings.
    
5.  Write your test cases in the `tests` directory, following the examples provided.
    
6.  Run the tests using the desired test runner (e.g., pytest).
    
7.  View the test execution reports in the `reports` directory.
    

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to submit a pull request or create an issue on GitHub.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

For any questions or inquiries, please contact souvik.dey.etce@gmail.com.