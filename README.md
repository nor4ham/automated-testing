#  Automated Testing Project

## Quick Start

1. **Clone the repo** and open in [VS Code](https://code.visualstudio.com/) with [Dev Containers](https://containers.dev/).
2. The environment will be auto-configured (Python, Java, Android SDK, Selenium, Appium, etc).
3. Run all tests:
   ```bash
   pytest web_testing/ mobile_testing/
   ```

4. Generate Allure report:
pytest --alluredir=Reports/allure-report
allure serve Reports/allure-report

5. Generate Pytest HTML report:
pytest --html=Reports/pytest-report.html

# Project Structure
.github/workflows/ci.yml       # CI/CD config
.devcontainer/                 # Dev Container config files
web_testing/                   # Selenium and API tests
mobile_testing/                # Appium mobile tests (iOS/Android)
Reports/                       # Test reports
README.md                      # Documentation


### Clean up old pycache files
find . -type d -name "__pycache__" -exec rm -rf {} +
cle