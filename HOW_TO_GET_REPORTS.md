# 📊 How to Get Load Test Reports

## Quick Answer

Reports are **automatically generated** when you run the tests!

---

## 🚀 Step-by-Step Guide

### Step 1: Run the Load Test

```bash
run_tests.bat
```

Or:

```bash
locust -f locustfile.py --config locust.conf
```

### Step 2: Wait for Test to Complete

The test will run for **3 minutes** (configured in `locust.conf`).

You'll see output like:
```
[2025-12-04 16:33:00] Starting Locust...
🔐 Performing ONE-TIME login...
✅ Global Bearer token saved.
[2025-12-04 16:33:05] Spawning 50 users at rate 5 users/s...
[2025-12-04 16:36:00] Test completed
```

### Step 3: Find Your Reports

After the test completes, reports are automatically saved to:

#### 📄 **HTML Report** (Visual, Interactive)
```
reports/html_reports/report.html
```

#### 📊 **CSV Reports** (Data Analysis)
```
reports/json_reports/locust_report_stats.csv
reports/json_reports/locust_report_stats_history.csv
reports/json_reports/locust_report_failures.csv
reports/json_reports/locust_report_exceptions.csv
```

---

## 📂 Opening the Reports

### HTML Report (Recommended for Quick Review)

**Option 1: Double-click**
- Navigate to: `d:\Load-test-using-python-locast\reports\html_reports\`
- Double-click `report.html`
- Opens in your default browser

**Option 2: Command line**
```bash
start reports\html_reports\report.html
```

**Option 3: VS Code**
- Right-click `report.html` in VS Code
- Select "Open with Live Server" or "Reveal in File Explorer"

### CSV Reports (For Data Analysis)

Open with Excel, Google Sheets, or any CSV viewer:
```bash
start reports\json_reports\locust_report_stats.csv
```

---

## 📊 What Each Report Contains

### 1. **HTML Report** (`report.html`)

**Visual dashboard with:**
- ✅ Total requests made
- ✅ Requests per second (RPS)
- ✅ Response times (min, max, average, percentiles)
- ✅ Failure rate
- ✅ Charts and graphs
- ✅ Request distribution by endpoint

**Perfect for:** Quick overview, presentations, sharing with team

---

### 2. **CSV Reports**

#### `locust_report_stats.csv`
**Summary statistics for each endpoint:**
- Request count
- Failure count
- Average response time
- Min/Max response time
- Percentiles (50th, 66th, 75th, 80th, 90th, 95th, 98th, 99th, 99.9th, 99.99th, 100th)
- Requests per second

#### `locust_report_stats_history.csv`
**Time-series data:**
- Statistics captured at regular intervals
- Shows how performance changed over time
- Useful for identifying performance degradation

#### `locust_report_failures.csv`
**Failed requests:**
- Which endpoints failed
- Error messages
- Number of occurrences

#### `locust_report_exceptions.csv`
**Exceptions during test:**
- Python exceptions that occurred
- Stack traces
- Useful for debugging

**Perfect for:** Detailed analysis, Excel charts, data processing

---

## 🎯 Example: What You'll See

### HTML Report Preview

```
┌─────────────────────────────────────────────────┐
│  LOCUST LOAD TEST REPORT                        │
├─────────────────────────────────────────────────┤
│  Total Requests:        15,000                  │
│  Failures:              0 (0%)                  │
│  Requests/sec:          83.33                   │
│  Average Response:      120 ms                  │
│  95th Percentile:       250 ms                  │
│  99th Percentile:       400 ms                  │
└─────────────────────────────────────────────────┘

Endpoint Performance:
┌──────────────────┬──────────┬──────────┬─────────┐
│ Name             │ Requests │ Failures │ Avg (ms)│
├──────────────────┼──────────┼──────────┼─────────┤
│ Dashboard        │  5,625   │    0     │   110   │
│ User Profile     │  3,750   │    0     │   125   │
│ Help Articles    │  3,750   │    0     │   115   │
│ PDF Generate     │  1,875   │    0     │   145   │
└──────────────────┴──────────┴──────────┴─────────┘
```

---

## 🔍 Analyzing Your Reports

### Key Metrics to Check

#### ✅ **Success Rate**
- Should be close to 100%
- If failures > 5%, investigate errors

#### ⏱️ **Response Times**
- **Average:** Should meet your SLA (e.g., < 200ms)
- **95th Percentile:** 95% of requests faster than this
- **99th Percentile:** Important for user experience

#### 📈 **Requests Per Second (RPS)**
- Shows throughput capacity
- Higher is better (if response times stay low)

#### 📊 **Distribution**
- Check if load is distributed as expected:
  - Dashboard: ~37.5% (weight 3)
  - User Profile: ~25% (weight 2)
  - Help Articles: ~25% (weight 2)
  - PDF Generate: ~12.5% (weight 1)

---

## 🛠️ Customizing Report Output

### Change Report Location

Edit `locust.conf`:
```ini
html=reports/my_custom_report.html
csv=reports/my_test_results
```

### Add Timestamp to Reports

Edit `run_tests.bat`:
```batch
@echo off
set TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%

locust -f locustfile.py ^
  --config locust.conf ^
  --html reports/html_reports/report_%TIMESTAMP%.html ^
  --csv reports/json_reports/locust_report_%TIMESTAMP%

pause
```

---

## 📧 Sharing Reports

### HTML Report
- Self-contained file
- Can be emailed or uploaded
- Opens in any browser
- No dependencies needed

### CSV Reports
- Import into Excel/Google Sheets
- Create custom charts
- Combine with other data sources

---

## 🎬 Real-Time Monitoring (Alternative)

If you want to **watch the test in real-time**, run with Web UI:

```bash
locust -f locustfile.py
```

Then open: **http://localhost:8089**

You can:
- ✅ See live statistics
- ✅ Watch charts update in real-time
- ✅ Download reports during/after test
- ✅ Stop/start test manually

---

## 📋 Quick Commands Reference

| Action | Command |
|--------|---------|
| Run test (auto-generate reports) | `run_tests.bat` |
| Open HTML report | `start reports\html_reports\report.html` |
| Open CSV in Excel | `start reports\json_reports\locust_report_stats.csv` |
| View report folder | `explorer reports\html_reports` |
| Run with Web UI | `locust -f locustfile.py` |

---

## ✅ Checklist

Before running:
- [ ] Test configuration is correct (`locust.conf`)
- [ ] Report directories exist (`reports/html_reports/`, `reports/json_reports/`)

After running:
- [ ] Check HTML report exists
- [ ] Review success rate (should be ~100%)
- [ ] Check response times meet requirements
- [ ] Look for any failures or exceptions
- [ ] Verify load distribution matches task weights

---

## 🎉 That's It!

**Reports are automatic!** Just run the test and check the `reports/` folder.

**Quick Start:**
1. Run: `run_tests.bat`
2. Wait 3 minutes
3. Open: `reports/html_reports/report.html`
4. Done! 🎊
