# Playwright Pytest Automation Suite

## 🛠 Tech Stack
- Python, Pytest, Playwright

## 📁 Project Structure
- `tests/` — all test files
- `pages/` — page object models
- `utils/` — helper/utility functions
- `data/` — test data files
- `assets/` — static assets

## ⚙️ Setup
1. Clone the repo
2. Create virtual env: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install deps: `pip install -r requirements.txt`
5. Install browsers: `playwright install`

## ▶️ Run Tests
pytest                        # all tests
pytest tests/test_login.py    # specific file
pytest --headed               # with browser visible
pytest --html=report.html     # with HTML report