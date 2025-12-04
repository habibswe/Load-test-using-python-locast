# Load Testing with Locust - Python

## Overview
This project performs load testing on multiple APIs with a **one-time login** approach. The authentication token is obtained once before all tests start and shared across all virtual users.

## Features
✅ **One-time global login** - Login happens once, not per user  
✅ **Multiple API testing** - Dashboard, Help, and PDF APIs tested concurrently  
✅ **Shared authentication** - All users share the same Bearer token  
✅ **Configurable load profiles** - Easy configuration via `locust.conf`

## Project Structure
```
├── apis/
│   ├── base_user.py          # Base class with authentication setup
│   ├── dashboard_api.py      # Dashboard API tests
│   ├── help_api.py           # Help Center API tests
│   └── pdf_api.py            # PDF Generation API tests
├── config/
│   ├── global_login.py       # One-time login handler
│   └── load_profiles.py      # Custom load test shapes
├── data/
│   ├── users.csv             # User credentials (if needed)
│   └── test_payloads.json    # Test data payloads
├── utils/
│   ├── csv_loader.py         # CSV data loader utility
│   └── report_generator.py   # Report generation utility
├── reports/                   # Generated test reports
├── locustfile.py             # Main Locust entry point
├── locust.conf               # Locust configuration
├── requirements.txt          # Python dependencies
└── run_tests.bat             # Windows batch script to run tests
```

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Test Parameters
Edit `locust.conf` to adjust:
- `host` - Target API host
- `users` - Number of concurrent users
- `spawn-rate` - Users spawned per second
- `run-time` - Test duration

### 3. Update Login Credentials
Edit `config/global_login.py` to set your login credentials:
```python
login_payload = {
    "email": "your-email@example.com",
    "password": "your-password"
}
```

## Running Tests

### Option 1: Using Batch Script (Windows)
```bash
run_tests.bat
```

### Option 2: Using Command Line
```bash
locust -f locustfile.py --config locust.conf
```

### Option 3: With Web UI
```bash
locust -f locustfile.py
# Then open http://localhost:8089 in your browser
```

## How It Works

### One-Time Login Flow
1. **Test Start Event** - Before any users spawn, `global_login.py` executes
2. **Login Request** - A single login request is made to get the Bearer token
3. **Token Storage** - The token is stored in `GLOBAL_TOKEN` variable
4. **User Spawn** - All virtual users use the same `GLOBAL_TOKEN` in their headers
5. **API Calls** - Users make concurrent API calls with shared authentication

### Multiple API Testing
The `locustfile.py` coordinates three API test classes:
- **DashboardAPI** - Tests dashboard and profile endpoints
- **HelpAPI** - Tests help center articles
- **PDFAPI** - Tests PDF generation

Each user randomly executes tasks from all three API classes, simulating realistic mixed workload.

## Configuration

### locust.conf
```ini
host=https://staging.amal.education
users=50
spawn-rate=5
run-time=3m
headless=true
html=reports/html_reports/report.html
csv=reports/json_reports/locust_report
```

## Reports
After test completion, reports are generated in:
- **HTML Report**: `reports/html_reports/report.html`
- **CSV Reports**: `reports/json_reports/locust_report_*.csv`

## Troubleshooting

### Login Fails
- Check credentials in `config/global_login.py`
- Verify the login endpoint URL
- Check if the API is accessible

### Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.7+ recommended)

### No Token in Requests
- Verify `GLOBAL_TOKEN` is set in `global_login.py`
- Check the login response structure matches `resp.json().get("access")`

## Adding New API Tests

1. Create a new file in `apis/` directory (e.g., `apis/new_api.py`)
2. Inherit from `BaseUser`
3. Define tasks with `@task` decorator
4. Add the class to `locustfile.py` tasks list

Example:
```python
from locust import task, between
from apis.base_user import BaseUser

class NewAPI(BaseUser):
    wait_time = between(1, 2)
    
    @task
    def test_endpoint(self):
        self.client.get("/api/new-endpoint/", name="New Endpoint")
```

## License
MIT
Run command:
python3 -m locust -f locustfile.py --config locust.conf
python3 -m locust -f locustfile.py --config locust.conf --headless --run-time 1m