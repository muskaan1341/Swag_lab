# Swag Lab Automation

This project provides automated end-to-end testing for the Swag Labs web application using Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern.

The framework is built for maintainability and scalability, ensuring test logic is clearly separated from page interactions. This makes the suite easy to extend, debug, and manage over time.

## Project Structure

```
Swag_lab/
│
├── pages/                # Page Object classes for each web page
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── tests/                # Automated test cases
│   ├── test_add_to_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   └── test_logout.py
│
├── utils/                # Utilities and configuration
│   ├── config.py
│   └── driver_factory.py
│
├── reports/              # HTML reports from test execution
│
├── conftest.py           # Shared pytest fixtures
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
```

## Setup

1. Clone the repository:

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run the full test suite:

```bash
pytest
```

Run tests with an HTML report:

```bash
pytest --html=reports/report.html
```

Run a specific test file with an HTML report:

```bash
pytest tests/<filename>.py --html=reports/report.html
```

## Framework Overview

- **Page Objects:** Each class in `pages/` contains element locators and reusable methods for a single page.
- **Tests:** Located in `tests/`, these files use page objects to perform actions and validate outcomes.
- **Fixtures:** Defined in `conftest.py`, they handle browser setup and teardown.

## Test Coverage

The suite covers the following scenarios:

### 1. Login
	- Valid and invalid credentials
	- Locked-out user
	- Problem user
	- Performance glitch user
	- Empty fields (username, password, both)
	- Special characters in credentials
	- Case sensitivity checks
	- Visual user

### 2. Add to Cart
	- Add one item
	- Add multiple items
	- Remove one item
	- Remove multiple items

### 3. Checkout
	- Valid information
	- Invalid information
	- Partially empty fields
	- All fields empty

### 4. Logout
	- From homepage
	- From cart page
	- From checkout page
	- Session cleared after logout (back button check)


pytest allows you to run the entire test suite at once and also generate an HTML report, which provides a clear view of all executed scripts in a single place.

It is especially useful when you want to run the suite in one go—for example, as part of morning smoke testing, sanity testing, or even regression testing. You just need to separate the scenarios based on the testing type (smoke, sanity, or regression).