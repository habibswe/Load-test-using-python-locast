# Project Structure

```
Load-test-using-python-locast/
│
├── 📄 locustfile.py              # Main load testing file (5 task sets)
├── 📄 config.py                  # Configuration settings
├── 📄 run_tests.py               # Convenient test runner script
├── 📄 requirements.txt           # Python dependencies
│
├── 📚 Documentation
│   ├── README.md                 # Comprehensive documentation
│   ├── QUICKSTART.md             # Quick start guide
│   └── PROJECT_SUMMARY.md        # Project summary
│
├── 🔧 Configuration
│   └── .gitignore                # Git ignore rules
│
└── 📊 Generated (after running tests)
    ├── *_report.html             # HTML test reports
    ├── *_stats.csv               # Statistics CSV
    ├── *_failures.csv            # Failures CSV
    └── *_exceptions.csv          # Exceptions CSV
```

## File Descriptions

### Core Files

- **locustfile.py**: Contains all test scenarios organized into 5 task sets:
  - AuthenticationTasks
  - DashboardTasks
  - AIAssistantTasks
  - LibraryTasks
  - HelpCenterTasks

- **config.py**: Centralized configuration for:
  - API endpoints
  - Test credentials
  - Task weights
  - Constants

- **run_tests.py**: Python script to run tests with:
  - Preset configurations (--quick, --medium, --stress)
  - Custom parameters
  - Automatic report generation

- **requirements.txt**: Python dependencies:
  - locust==2.20.0
  - faker==22.0.0
  - requests==2.31.0

### Documentation

- **README.md**: Full documentation with installation, usage, and customization
- **QUICKSTART.md**: Quick 3-step setup guide
- **PROJECT_SUMMARY.md**: Complete project overview

### Configuration

- **.gitignore**: Excludes test reports, Python cache, and IDE files

## Task Set Architecture

```
AmalEducationUser (Main User Class)
│
├── AuthenticationTasks (Weight: 1)
│   ├── sign_up()
│   ├── sign_in()
│   └── refresh_token_endpoint()
│
├── DashboardTasks (Weight: 3)
│   ├── get_dashboard_insights()
│   └── search_anything()
│
├── AIAssistantTasks (Weight: 2)
│   ├── get_tools_and_templates()
│   ├── get_random_mystery_box()
│   ├── create_thread()
│   └── get_my_collections()
│
├── LibraryTasks (Weight: 2)
│   ├── get_library_data()
│   └── create_collection()
│
└── HelpCenterTasks (Weight: 1)
    ├── get_help_articles()
    └── submit_contact_us()
```

## Test Flow

```
1. User starts test
   ↓
2. Locust spawns users (based on -u parameter)
   ↓
3. Each user randomly selects a task set (weighted)
   ↓
4. Task set executes in sequence
   ↓
5. User waits 1-3 seconds
   ↓
6. Repeat from step 3
   ↓
7. Test ends (based on -t parameter or manual stop)
   ↓
8. Generate reports
```

## API Endpoint Coverage

```
Amal Education API
│
├── /api/accounts/
│   ├── sign-up/              ✅ Tested
│   ├── sign-in/              ✅ Tested
│   └── token/refresh/        ✅ Tested
│
├── /api/dashboard/
│   ├── /                     ✅ Tested
│   └── v2/search/            ✅ Tested
│
├── /api/ai-assistant/
│   ├── tools-and-template/   ✅ Tested
│   ├── random-mystery-box/   ✅ Tested
│   ├── chat/thread/          ✅ Tested
│   ├── my-collection/        ✅ Tested
│   ├── library/              ✅ Tested
│   └── create-collection/    ✅ Tested
│
└── /api/help-center/
    ├── help-articles/        ✅ Tested
    └── contact-us/           ✅ Tested
```

## Usage Workflow

```
┌─────────────────────────────────────────┐
│  1. Install Dependencies                │
│  python3 -m pip install -r requirements │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  2. Choose Test Type                    │
│  • Web UI: python3 run_tests.py         │
│  • Quick:  python3 run_tests.py --quick │
│  • Custom: python3 run_tests.py -u 50   │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  3. Locust Runs Tests                   │
│  • Spawns users                         │
│  • Executes tasks                       │
│  • Collects metrics                     │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  4. View Results                        │
│  • HTML report                          │
│  • CSV data                             │
│  • Web UI (if applicable)               │
└─────────────────────────────────────────┘
```

## Quick Reference

### Run Commands

```bash
# Web UI (interactive)
python3 run_tests.py

# Quick test (10 users, 1 min)
python3 run_tests.py --quick

# Medium test (50 users, 5 min)
python3 run_tests.py --medium

# Stress test (100 users, 10 min)
python3 run_tests.py --stress

# Custom test
python3 run_tests.py --headless -u 25 -r 5 -t 120s --html report.html
```

### Direct Locust Commands

```bash
# Web UI
python3 -m locust -f locustfile.py --host=https://backend.amal.education

# Headless
python3 -m locust -f locustfile.py --host=https://backend.amal.education --headless -u 10 -r 2 -t 60s

# With reports
python3 -m locust -f locustfile.py --host=https://backend.amal.education --headless -u 10 -r 2 -t 60s --html=report.html --csv=results
```

### Key Metrics

- **RPS**: Requests per second (higher is better)
- **Response Time**: Average response time (lower is better)
- **Failure Rate**: Percentage of failed requests (should be 0%)
- **95th Percentile**: 95% of requests complete within this time

### Configuration Files

- **API Token**: `config.py` → `API_TOKEN`
- **Test User**: `config.py` → `TEST_USERS`
- **Task Weights**: `locustfile.py` → `AmalEducationUser.tasks`
- **Wait Time**: `locustfile.py` → `wait_time = between(1, 3)`
