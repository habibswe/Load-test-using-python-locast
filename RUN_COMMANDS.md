# 🚀 Locust Test Run Commands - সব Command এক জায়গায়

## 📋 Table of Contents
1. [UI Mode Commands](#ui-mode-commands)
2. [Headless Mode Commands](#headless-mode-commands)
3. [Specific API Commands](#specific-api-commands)
4. [Quick Reference](#quick-reference)

---

## 🖥️ UI Mode Commands

### সব API একসাথে (Web UI)
```bash
python3 -m locust -f locustfile.py --host=https://backend.amal.education
```
তারপর browser এ যান: **http://localhost:8089**

### শুধু Dashboard API (Web UI)
```bash
python3 -m locust -f locustfile.py DashboardAPI --host=https://backend.amal.education
```

### শুধু Help API (Web UI)
```bash
python3 -m locust -f locustfile.py HelpAPI --host=https://backend.amal.education
```

### শুধু AI Assistant API (Web UI)
```bash
python3 -m locust -f locustfile.py AIAssistantAPI --host=https://backend.amal.education
```

### শুধু Authentication API (Web UI)
```bash
python3 -m locust -f locustfile.py AuthenticationAPI --host=https://backend.amal.education
```

### শুধু Library API (Web UI)
```bash
python3 -m locust -f locustfile.py LibraryAPI --host=https://backend.amal.education
```

---

## 🤖 Headless Mode Commands

### সব API একসাথে (Headless)

#### Quick Test (10 users, 1 minute)
```bash
python3 -m locust -f locustfile.py \
  --host=https://backend.amal.education \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html quick_test_report.html \
  --csv quick_test_results
```

#### Medium Test (50 users, 5 minutes)
```bash
python3 -m locust -f locustfile.py \
  --host=https://backend.amal.education \
  --headless \
  -u 50 \
  -r 5 \
  -t 300s \
  --html medium_test_report.html \
  --csv medium_test_results
```

#### Stress Test (100 users, 10 minutes)
```bash
python3 -m locust -f locustfile.py \
  --host=https://backend.amal.education \
  --headless \
  -u 100 \
  -r 10 \
  -t 600s \
  --html stress_test_report.html \
  --csv stress_test_results
```

---

## 🎯 Specific API Commands

### Dashboard API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py DashboardAPI --host=https://backend.amal.education
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py DashboardAPI \
  --host=https://backend.amal.education \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html dashboard_report.html
```

---

### Help API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py HelpAPI --host=https://backend.amal.education
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py HelpAPI \
  --host=https://backend.amal.education \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html help_report.html
```

---

### AI Assistant API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py AIAssistantAPI --host=https://backend.amal.education
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py AIAssistantAPI \
  --host=https://backend.amal.education \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html ai_assistant_report.html
```

---

### Authentication API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py AuthenticationAPI --host=https://backend.amal.education
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py AuthenticationAPI \
  --host=https://backend.amal.education \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html auth_report.html
```

---

### Library API Only

#### UI Mode
```bash
python3 -m locust -f locustfile.py LibraryAPI --host=https://backend.amal.education
```

#### Headless Mode
```bash
python3 -m locust -f locustfile.py LibraryAPI \
  --host=https://backend.amal.education \
  --headless \
  -u 10 \
  -r 2 \
  -t 60s \
  --html library_report.html
```

---

## 📊 Quick Reference

### Parameters ব্যাখ্যা:

| Parameter | অর্থ | Example |
|-----------|------|---------|
| `-f` | Locustfile path | `-f locustfile.py` |
| `--host` | API base URL | `--host=https://backend.amal.education` |
| `--headless` | UI ছাড়া run করবে | `--headless` |
| `-u` | Total users | `-u 10` |
| `-r` | Spawn rate (users/sec) | `-r 2` |
| `-t` | Run time | `-t 60s` (60 seconds) |
| `--html` | HTML report file | `--html report.html` |
| `--csv` | CSV results prefix | `--csv results` |

### Time Format:
- `60s` = 60 seconds
- `5m` = 5 minutes
- `1h` = 1 hour

---

## 🎨 UI Mode এ কিভাবে ব্যবহার করবেন?

### Step 1: Command Run করুন
```bash
python3 -m locust -f locustfile.py --host=https://backend.amal.education
```

### Step 2: Browser Open করুন
যান: **http://localhost:8089**

### Step 3: Configuration দিন
- **Number of users**: 10
- **Spawn rate**: 2
- **Host**: https://backend.amal.education (already set)

### Step 4: Start করুন
"Start swarming" button এ click করুন

### Step 5: Monitor করুন
- **Statistics** tab: Request count, response time দেখুন
- **Charts** tab: Real-time graphs দেখুন
- **Failures** tab: Errors দেখুন

### Step 6: Stop করুন
"Stop" button এ click করুন

---

## 💡 Recommended Commands

### 🔰 শুরুতে (UI Mode):
```bash
python3 -m locust -f locustfile.py HelpAPI --host=https://backend.amal.education
```
Browser এ: http://localhost:8089

### 🚀 Quick Test (Headless):
```bash
python3 -m locust -f locustfile.py HelpAPI \
  --host=https://backend.amal.education \
  --headless \
  -u 5 \
  -r 1 \
  -t 30s \
  --html help_quick.html
```

### 📈 Full Test (Headless):
```bash
python3 -m locust -f locustfile.py \
  --host=https://backend.amal.education \
  --headless \
  -u 20 \
  -r 5 \
  -t 120s \
  --html full_test.html \
  --csv full_test
```

---

## 🔧 Custom Commands

### আপনার নিজের configuration:
```bash
python3 -m locust -f locustfile.py [API_CLASS] \
  --host=https://backend.amal.education \
  --headless \
  -u [USERS] \
  -r [SPAWN_RATE] \
  -t [TIME] \
  --html [REPORT_NAME].html
```

### Example:
```bash
python3 -m locust -f locustfile.py DashboardAPI \
  --host=https://backend.amal.education \
  --headless \
  -u 25 \
  -r 5 \
  -t 90s \
  --html my_dashboard_test.html
```

---

## 📝 Notes

1. **UI Mode** - Interactive, real-time monitoring
2. **Headless Mode** - Automated, generates reports
3. **Specific API** - শুধু একটা API test করতে চাইলে
4. **All APIs** - সব API একসাথে test করতে চাইলে

---

## 🎯 আপনার জন্য সবচেয়ে ভালো Command:

### UI Mode এ সব API test:
```bash
python3 -m locust -f locustfile.py --host=https://backend.amal.education
```

### UI Mode এ শুধু Help API:
```bash
python3 -m locust -f locustfile.py HelpAPI --host=https://backend.amal.education
```

Browser এ যান: **http://localhost:8089** এবং test start করুন! 🚀
