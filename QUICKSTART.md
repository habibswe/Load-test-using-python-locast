# Quick Start Guide - Amal Education API Load Testing

## 🚀 Quick Setup (3 steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Your First Test

**Option A: Web UI (Recommended for first-time users)**
```bash
python run_tests.py
```
Then open http://localhost:8089 in your browser.

**Option B: Quick Automated Test**
```bash
python run_tests.py --quick
```

### 3. View Results
- Web UI: Real-time charts at http://localhost:8089
- Reports: Check `quick_test_report.html` in your browser
- CSV Data: `quick_test_results_*.csv` files

---

## 📊 Preset Test Configurations

### Quick Test (1 minute)
```bash
python run_tests.py --quick
```
- 10 users
- 2 users/second spawn rate
- 1 minute duration
- Generates HTML report

### Medium Test (5 minutes)
```bash
python run_tests.py --medium
```
- 50 users
- 5 users/second spawn rate
- 5 minutes duration
- Generates HTML report

### Stress Test (10 minutes)
```bash
python run_tests.py --stress
```
- 100 users
- 10 users/second spawn rate
- 10 minutes duration
- Generates HTML report

---

## 🎯 What Gets Tested?

The load test simulates real users performing these actions:

1. **Authentication** (10%)
   - Sign up
   - Sign in
   - Token refresh

2. **Dashboard** (30%)
   - View daily insights
   - Search functionality

3. **AI Assistant** (20%)
   - Browse tools & templates
   - Create chat threads
   - View collections

4. **Library** (20%)
   - Browse library
   - Create collections

5. **Help Center** (10%)
   - View help articles
   - Submit contact forms

---

## 🛠️ Custom Test Configuration

Run with custom parameters:

```bash
python run_tests.py --headless -u 25 -r 5 -t 120s --html my_report.html
```

Parameters:
- `-u 25`: 25 concurrent users
- `-r 5`: Spawn 5 users per second
- `-t 120s`: Run for 120 seconds
- `--html my_report.html`: Save HTML report

---

## 📈 Understanding Results

### Key Metrics to Watch:

1. **Requests/sec (RPS)**: Higher is better
2. **Response Time**: Lower is better
   - Excellent: < 200ms
   - Good: < 500ms
   - Acceptable: < 1000ms
   - Slow: > 2000ms
3. **Failure Rate**: Should be 0% or very low
4. **95th Percentile**: 95% of requests complete within this time

### Good Results Example:
```
Requests/sec: 50-100
Avg Response Time: 200-500ms
Failure Rate: 0%
```

---

## ⚠️ Important Notes

1. **Test Environment**: Always test against a test/staging environment, NOT production
2. **API Token**: Update the API token in `config.py` if needed
3. **Test Users**: Use dedicated test accounts
4. **Server Monitoring**: Monitor your server resources during tests
5. **Start Small**: Begin with low user counts and increase gradually

---

## 🔧 Troubleshooting

### Problem: "Module not found" error
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Problem: Connection refused
**Solution**: Check if the API is running and accessible
```bash
curl https://backend.amal.education/api/accounts/health-check/
```

### Problem: High failure rate
**Solution**: 
- Reduce number of users
- Increase wait time between requests
- Check server capacity

---

## 📚 Next Steps

1. Review the full [README.md](README.md) for detailed documentation
2. Customize test scenarios in `locustfile.py`
3. Adjust configuration in `config.py`
4. Set up continuous load testing in your CI/CD pipeline

---

## 💡 Pro Tips

- **Gradual Ramp-up**: Start with 10 users, then 50, then 100
- **Monitor Both Sides**: Watch both Locust metrics and server metrics
- **Save Reports**: Keep HTML reports for comparison over time
- **Test Regularly**: Run load tests before major releases
- **Realistic Data**: Use realistic test data that matches production patterns

---

## 🆘 Need Help?

Check the detailed [README.md](README.md) or Locust documentation:
- https://docs.locust.io/
