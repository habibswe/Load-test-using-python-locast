# Project Setup Summary

## ✅ What Has Been Created

### Core Files
1. **locustfile.py** - Main load testing file with 5 task sets:
   - AuthenticationTasks (Sign up, Sign in, Token refresh)
   - DashboardTasks (Dashboard insights, Search)
   - AIAssistantTasks (Tools, Mystery box, Threads, Collections)
   - LibraryTasks (Library data, Create collections)
   - HelpCenterTasks (Help articles, Contact form)

2. **config.py** - Configuration file with:
   - API endpoints
   - Test credentials
   - Task weights
   - Constants

3. **requirements.txt** - Python dependencies:
   - locust==2.20.0
   - faker==22.0.0
   - requests==2.31.0

4. **run_tests.py** - Convenient test runner with presets:
   - Quick test (10 users, 1 min)
   - Medium test (50 users, 5 min)
   - Stress test (100 users, 10 min)

5. **README.md** - Comprehensive documentation
6. **QUICKSTART.md** - Quick start guide
7. **.gitignore** - Git ignore rules

## ✅ Dependencies Installed

All required dependencies are now installed:
- ✓ locust (2.34.0)
- ✓ requests (2.32.5)
- ✓ faker (37.12.0)

## 🚀 How to Run

### Option 1: Web UI (Recommended)
```bash
python3 run_tests.py
```
Then open http://localhost:8089

### Option 2: Quick Test
```bash
python3 run_tests.py --quick
```

### Option 3: Direct Locust Command
```bash
locust -f locustfile.py --host=https://backend.amal.education
```

## 📊 Test Coverage

The load tests cover these API endpoints from your Postman collection:

### Accounts (Authentication)
- ✓ Sign Up
- ✓ Sign In
- ✓ Token Refresh
- ✓ Profile Setup
- ✓ Change Password

### Dashboard
- ✓ Dashboard Daily Insights
- ✓ Search Anything

### AI Assistant
- ✓ Tools & Templates
- ✓ Random Mystery Box
- ✓ Thread Create
- ✓ Thread Chat
- ✓ My Collections

### Library
- ✓ Library Data
- ✓ Collection Create
- ✓ Collection Details
- ✓ Folder Operations

### Help Center
- ✓ Help Articles
- ✓ Contact Us

## 🎯 Task Distribution

Tasks are weighted to simulate realistic user behavior:
- Dashboard: 30% (weight: 3)
- AI Assistant: 20% (weight: 2)
- Library: 20% (weight: 2)
- Help Center: 10% (weight: 1)
- Authentication: 10% (weight: 1)

## ⚙️ Configuration

### API Settings
- **Host**: https://backend.amal.education
- **API Token**: 7ca7c0a9-4d15-4697-81ae-e0b9ded2502d
- **Test User**: mirazhs@proton.me

### Load Test Defaults
- **Users**: 10
- **Spawn Rate**: 2 users/second
- **Wait Time**: 1-3 seconds between requests

## 📈 Expected Results

For a healthy API, you should see:
- **Response Time**: < 500ms average
- **Failure Rate**: < 1%
- **Requests/sec**: 20-50 (for 10 users)

## 🔧 Customization

### Change Test User
Edit `config.py`:
```python
TEST_USERS = [
    {
        "email": "your-test-user@example.com",
        "password": "your-password"
    }
]
```

### Adjust Task Weights
Edit `locustfile.py`:
```python
tasks = {
    DashboardTasks: 5,  # Increase dashboard testing
    AIAssistantTasks: 1,  # Reduce AI testing
    # ...
}
```

### Change Wait Time
Edit `locustfile.py`:
```python
wait_time = between(2, 5)  # Wait 2-5 seconds
```

## 🎓 Next Steps

1. **Run a quick test** to verify everything works:
   ```bash
   python3 run_tests.py --quick
   ```

2. **Review the HTML report** generated after the test

3. **Gradually increase load**:
   - Start with 10 users
   - Then try 25 users
   - Then 50 users
   - Monitor server resources

4. **Customize for your needs**:
   - Add more endpoints
   - Adjust task weights
   - Create custom test scenarios

## 📚 Documentation

- **QUICKSTART.md** - Quick start guide
- **README.md** - Full documentation
- **config.py** - Configuration reference
- **locustfile.py** - Test scenarios (well-commented)

## ⚠️ Important Notes

1. **Test Environment**: Always test against staging/test environment
2. **API Token**: Update if the token expires
3. **Server Monitoring**: Watch server CPU/memory during tests
4. **Gradual Ramp-up**: Start small and increase gradually
5. **Data Cleanup**: Clean up test data after load testing

## 🆘 Troubleshooting

### Issue: Import errors
**Solution**: Ensure all dependencies are installed
```bash
python3 -m pip install -r requirements.txt
```

### Issue: Connection refused
**Solution**: Verify API is accessible
```bash
curl https://backend.amal.education/api/accounts/health-check/
```

### Issue: High failure rate
**Solution**: 
- Reduce number of users
- Check API token is valid
- Verify test credentials

## ✨ Features

- ✅ Realistic user behavior simulation
- ✅ Multiple test scenarios
- ✅ Configurable load patterns
- ✅ HTML and CSV reports
- ✅ Easy-to-use presets
- ✅ Well-documented code
- ✅ Modular task structure
- ✅ Authentication handling
- ✅ Error handling and retries

## 🎉 You're Ready!

Everything is set up and ready to go. Start with:

```bash
python3 run_tests.py --quick
```

Good luck with your load testing! 🚀
