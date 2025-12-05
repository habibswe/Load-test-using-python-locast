# Load Testing for Amal Education API

This project contains load testing scripts for the Amal Education API using Python and Locust.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── locustfile.py          # Main Locust load testing file
├── requirements.txt       # Python dependencies
├── config.py             # Configuration file (optional)
└── README.md             # This file
```

## Running the Tests

### Basic Usage

To run Locust with the web UI:

```bash
locust -f locustfile.py --host=https://backend.amal.education
```

Then open your browser and navigate to `http://localhost:8089` to access the Locust web interface.

### Headless Mode

To run Locust without the web UI (headless mode):

```bash
locust -f locustfile.py --host=https://backend.amal.education --headless -u 10 -r 2 -t 60s
```

Parameters:
- `-u 10`: Number of users to simulate (10 users)
- `-r 2`: Spawn rate (2 users per second)
- `-t 60s`: Test duration (60 seconds)

### Advanced Options

Run with specific number of users and spawn rate:

```bash
locust -f locustfile.py --host=https://backend.amal.education -u 50 -r 5
```

Run with HTML report generation:

```bash
locust -f locustfile.py --host=https://backend.amal.education --headless -u 10 -r 2 -t 60s --html=report.html
```

Run with CSV output:

```bash
locust -f locustfile.py --host=https://backend.amal.education --headless -u 10 -r 2 -t 60s --csv=results
```

## Test Scenarios

The load testing suite includes the following test scenarios:

### 1. Authentication Tasks
- User registration (sign-up)
- User login (sign-in)
- Token refresh

### 2. Dashboard Tasks
- Get dashboard daily insights
- Search functionality

### 3. AI Assistant Tasks
- Get tools and templates
- Get random mystery box
- Create chat threads
- Get user collections

### 4. Library Tasks
- Get library data
- Create collections

### 5. Help Center Tasks
- Get help articles
- Submit contact us form

## Task Weights

The tasks are weighted as follows:
- Dashboard Tasks: 3
- AI Assistant Tasks: 2
- Library Tasks: 2
- Help Center Tasks: 1
- Authentication Tasks: 1

This means Dashboard tasks will be executed more frequently during the load test.

## Configuration

### API Token

The API token is currently hardcoded in the script:
```python
"X-API-Token": "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"
```

### Test User Credentials

Default test user credentials:
- Email: `mirazhs@proton.me`
- Password: `testing321`

**Note:** For production load testing, you should use test accounts and update these credentials.

## Customization

### Adjusting Wait Time

Modify the `wait_time` in the `AmalEducationUser` class:

```python
wait_time = between(1, 3)  # Wait 1-3 seconds between tasks
```

### Changing Task Weights

Modify the `tasks` dictionary in the `AmalEducationUser` class:

```python
tasks = {
    DashboardTasks: 3,
    AIAssistantTasks: 2,
    LibraryTasks: 2,
    HelpCenterTasks: 1,
    AuthenticationTasks: 1
}
```

### Running Specific Task Sets

To run only specific task sets, modify the `tasks` dictionary or create a new user class:

```python
class DashboardOnlyUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [DashboardTasks]
```

Then run:
```bash
locust -f locustfile.py DashboardOnlyUser --host=https://backend.amal.education
```

## Monitoring and Results

### Web UI Metrics

When using the web UI, you can monitor:
- Number of users
- Requests per second (RPS)
- Response times (min, max, median, average)
- Failure rate
- Charts and graphs

### Report Files

Generated reports include:
- HTML report: Visual representation of test results
- CSV files: Raw data for further analysis
  - `results_stats.csv`: Request statistics
  - `results_failures.csv`: Failed requests
  - `results_exceptions.csv`: Exceptions encountered

## Best Practices

1. **Start Small**: Begin with a small number of users and gradually increase
2. **Monitor Server**: Keep an eye on server resources during testing
3. **Test Environment**: Use a dedicated test environment, not production
4. **Realistic Scenarios**: Ensure test scenarios match real user behavior
5. **Data Cleanup**: Clean up test data after load testing

## Troubleshooting

### Common Issues

1. **Connection Errors**
   - Verify the host URL is correct
   - Check network connectivity
   - Ensure the API is running

2. **Authentication Failures**
   - Verify API token is valid
   - Check user credentials
   - Ensure the authentication endpoint is correct

3. **High Failure Rate**
   - Reduce the number of concurrent users
   - Increase wait time between requests
   - Check server capacity

## Example Commands

### Quick Test (10 users, 1 minute)
```bash
locust -f locustfile.py --host=https://backend.amal.education --headless -u 10 -r 2 -t 60s
```

### Medium Test (50 users, 5 minutes)
```bash
locust -f locustfile.py --host=https://backend.amal.education --headless -u 50 -r 5 -t 300s --html=report.html
```

### Stress Test (100 users, 10 minutes)
```bash
locust -f locustfile.py --host=https://backend.amal.education --headless -u 100 -r 10 -t 600s --html=stress_report.html --csv=stress_results
```

### Interactive Web UI
```bash
locust -f locustfile.py --host=https://backend.amal.education
```

## Additional Resources

- [Locust Documentation](https://docs.locust.io/)
- [Locust Best Practices](https://docs.locust.io/en/stable/writing-a-locustfile.html)
- [Performance Testing Guide](https://docs.locust.io/en/stable/quickstart.html)

## License

This project is for testing purposes only.