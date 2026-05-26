# 🎭 Playwright Pytest Automation Suite

> A portfolio-grade end-to-end test automation framework built with **Python**, **Pytest**, and **Playwright** — structured for scalability, readability, and CI/CD readiness.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.58.0-2EAD33?style=flat&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.0.2-0A9EDC?style=flat&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 📌 Overview

This framework demonstrates industry-standard automation practices for web applications. It follows the **Page Object Model (POM)** design pattern, supports **parallel test execution**, and generates detailed **HTML reports** — making it suitable for real-world QA workflows and CI/CD pipelines.

**Key highlights:**
- Clean separation of concerns via Page Object Model
- Parallel test execution with `pytest-xdist`
- HTML reporting with `pytest-html` and metadata support
- Configurable base URL for multi-environment testing
- Headed and headless browser support (Chromium, Firefox)
- Reusable utility functions and shared fixtures via `conftest.py`

---

## 🛠 Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Core language |
| Playwright | 1.58.0 | Browser automation |
| Pytest | 9.0.2 | Test runner & framework |
| pytest-playwright | 0.7.2 | Playwright–Pytest integration |
| pytest-xdist | 3.8.0 | Parallel test execution |
| pytest-html | 4.2.0 | HTML test reporting |
| pytest-base-url | 2.1.0 | Configurable base URL |
| pytest-metadata | 3.1.1 | Report metadata enrichment |
| requests | 2.32.5 | HTTP/API utility calls |

---

## 📁 Project Structure

```
playwright-pytest-automation/
│
├── pages/              # Page Object Models (one class per page)
├── tests/              # Test files (organized by feature/module)
├── utils/              # Reusable helper functions and constants
├── assets/             # Static test assets (images, files, etc.)
│
├── conftest.py         # Shared fixtures and Playwright setup
├── pytest.ini          # Pytest configuration (markers, base URL, options)
├── requirements.txt    # Pinned Python dependencies
└── README.md
```

**Design pattern:** Each page of the application under test has a corresponding class in `pages/` that encapsulates its locators and actions. Tests in `tests/` interact only with page objects — keeping tests clean and maintainable.

---

## ⚙️ Setup

### Prerequisites
- Python 3.10 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/AmirthaRS/playwright-pytest-automation.git
cd playwright-pytest-automation

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install
```

---

## ▶️ Running Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_login.py

# Run with browser visible (headed mode)
pytest --headed

# Run tests in parallel (4 workers)
pytest -n 4

# Run on a specific browser
pytest --browser firefox
pytest --browser webkit

# Generate an HTML report
pytest --html=reports/report.html --self-contained-html

# Run against a different environment
pytest --base-url https://staging.example.com

# Combine options
pytest --headed --browser chromium -n 2 --html=reports/report.html
```

---

## 📊 Test Reports

After running tests with the `--html` flag, open the generated report in your browser:

```bash
# Example
pytest --html=reports/report.html --self-contained-html
open reports/report.html        # macOS
start reports/report.html       # Windows
```

Reports include test status, duration, failure screenshots (if configured), and environment metadata.

---

## 🧩 Key Concepts

### Page Object Model
Each page is represented as a Python class with locators and action methods:

```python
# pages/login_page.py (example)
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
```

### Fixtures (`conftest.py`)
Shared setup and teardown logic (browser launch, page creation, test data) is centralised in `conftest.py` and injected into tests via Pytest fixtures.

---

## 🚀 CI/CD Integration

This framework is CI/CD ready. Example GitHub Actions workflow:

```yaml
name: Playwright Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps
      - name: Run tests
        run: pytest --html=report.html --self-contained-html
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: test-report
          path: report.html
```

---

## 📂 Writing a New Test

1. Create a page object in `pages/` if the page isn't already covered.
2. Add your test file in `tests/` following the naming convention `test_<feature>.py`.
3. Use fixtures from `conftest.py` for browser and page setup.
4. Run and verify locally before pushing.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 👤 Author

**Amirtha RS**
- GitHub: [@AmirthaRS](https://github.com/AmirthaRS)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
