# Swag Lab Automation

This project automates end-to-end testing for the Swag Labs web application using Selenium, Pytest, and the Page Object Model (POM) design pattern.

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
├── tests/                # Test cases for different scenarios
│   ├── test_add_to_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   └── test_logout.py
│
├── utils/                # Utilities and configuration
│   ├── config.py
│   └── driver_factory.py
│
├── reports/              # Test execution reports (HTML)
│
├── conftest.py           # Pytest fixtures
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup

1. **Clone the repository**
	```
	git clone <your-repo-url>
	cd Swag_lab
	```

2. **Install dependencies**
	```
	pip install -r requirements.txt
	```

3. **Configure settings**
	- Edit `utils/config.py` to set your base URL and credentials.

## Running Tests

- To run all tests:
  ```
  pytest
  ```

- To generate an HTML report:
  ```
  pytest --html=reports/report.html
  ```

## How It Works

- **Page Objects:** Each page class in `pages/` encapsulates locators and actions for a specific page.
- **Tests:** Each test in `tests/` uses these page objects to perform actions and assertions.
- **Fixtures:** `conftest.py` and test files use fixtures for browser setup and teardown.

## Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes
4. Push to the branch
5. Open a pull request
