# Modular API Structure - বাংলায় ব্যাখ্যা

## 📁 Project Structure (প্রজেক্ট স্ট্রাকচার)

```
Load-test-using-python-locast/
│
├── apis/                          # সব API test files এখানে
│   ├── base_user.py              # Base class - authentication handle করে
│   ├── authentication_api.py     # Sign up, Sign in, Token refresh
│   ├── dashboard_api.py          # Dashboard এবং Search tests
│   ├── ai_assistant_api.py       # AI Assistant tests
│   ├── library_api.py            # Library এবং Collection tests
│   └── help_api.py               # Help Center tests
│
├── config/                        # Configuration files
│   ├── global_login.py           # One-time login setup
│   └── load_profiles.py          # Load test profiles
│
├── locustfile.py                 # Main file - সব API import করে
├── run_tests.py                  # Test run করার script
└── requirements.txt              # Dependencies
```

## 🎯 কিভাবে কাজ করে?

### 1. Base User (base_user.py)
- সব API test class এর parent
- Authentication handle করে
- Common headers set করে
- Login করে token নেয়

### 2. Individual API Files
প্রতিটি API এর জন্য আলাদা file:

#### authentication_api.py
```python
class AuthenticationAPI(BaseUser):
    @task(1)
    def sign_up(self):
        # Sign up test
    
    @task(2)
    def sign_in(self):
        # Sign in test
    
    @task(1)
    def refresh_token(self):
        # Token refresh test
```

#### dashboard_api.py
```python
class DashboardAPI(BaseUser):
    @task(3)
    def get_dashboard_insights(self):
        # Dashboard test
    
    @task(2)
    def search_anything(self):
        # Search test
```

#### ai_assistant_api.py
```python
class AIAssistantAPI(BaseUser):
    @task(2)
    def get_tools_and_templates(self):
        # Tools test
    
    @task(2)
    def get_random_mystery_box(self):
        # Mystery box test
    
    @task(1)
    def create_thread(self):
        # Thread creation test
    
    @task(2)
    def get_my_collections(self):
        # Collections test
```

#### library_api.py
```python
class LibraryAPI(BaseUser):
    @task(2)
    def get_library_data(self):
        # Library data test
    
    @task(1)
    def create_collection(self):
        # Collection creation test
```

#### help_api.py
```python
class HelpAPI(BaseUser):
    @task(2)
    def get_help_articles(self):
        # Help articles test
    
    @task(1)
    def submit_contact_us(self):
        # Contact form test
```

### 3. Main Locustfile
সব API class import করে:
```python
from apis.authentication_api import AuthenticationAPI
from apis.dashboard_api import DashboardAPI
from apis.ai_assistant_api import AIAssistantAPI
from apis.library_api import LibraryAPI
from apis.help_api import HelpAPI
```

## 🚀 কিভাবে Run করবেন?

### সব API একসাথে test করতে:
```bash
python3 run_tests.py --quick
```
অথবা
```bash
python3 -m locust -f locustfile.py --host=https://backend.amal.education
```

### শুধু একটি API test করতে:

#### শুধু Dashboard test:
```bash
python3 -m locust -f locustfile.py DashboardAPI --host=https://backend.amal.education
```

#### শুধু Help Center test:
```bash
python3 -m locust -f locustfile.py HelpAPI --host=https://backend.amal.education
```

#### শুধু AI Assistant test:
```bash
python3 -m locust -f locustfile.py AIAssistantAPI --host=https://backend.amal.education
```

#### শুধু Authentication test:
```bash
python3 -m locust -f locustfile.py AuthenticationAPI --host=https://backend.amal.education
```

#### শুধু Library test:
```bash
python3 -m locust -f locustfile.py LibraryAPI --host=https://backend.amal.education
```

## 📊 Task Weights কি?

`@task(number)` দিয়ে বলা হয় কতবার execute হবে:

```python
@task(3)  # 3 বার execute হবে
def get_dashboard_insights(self):
    pass

@task(1)  # 1 বার execute হবে
def search_anything(self):
    pass
```

উপরের example এ, dashboard insights 3 বার call হবে যখন search 1 বার call হবে।

## 🔧 নতুন Endpoint যোগ করতে চান?

### উদাহরণ: Dashboard এ নতুন endpoint যোগ করা

`apis/dashboard_api.py` file খুলুন এবং যোগ করুন:

```python
@task(1)
def get_notifications(self):
    """Test notifications endpoint"""
    self.client.get(
        "/api/accounts/notifications/",
        name="Dashboard - Notifications"
    )
```

### উদাহরণ: নতুন API file তৈরি করা

যদি Accounts API এর জন্য আলাদা file চান:

1. নতুন file তৈরি করুন: `apis/accounts_api.py`

```python
from locust import task, between
from apis.base_user import BaseUser

class AccountsAPI(BaseUser):
    wait_time = between(1, 3)

    @task
    def get_profile_information(self):
        self.client.get(
            "/api/accounts/profile-information/",
            name="Accounts - Profile Info"
        )
    
    @task
    def update_profile(self):
        payload = {
            "firstName": "Test",
            "lastName": "User"
        }
        self.client.put(
            "/api/accounts/update-profile/",
            json=payload,
            name="Accounts - Update Profile"
        )
```

2. `locustfile.py` তে import করুন:

```python
from apis.accounts_api import AccountsAPI
```

## ✅ সুবিধা (Advantages)

1. **Organized**: প্রতিটি API আলাদা file এ
2. **Easy to maintain**: একটা API change করলে শুধু সেই file change করতে হবে
3. **Selective testing**: যেকোনো একটা API আলাদা test করা যায়
4. **Reusable**: BaseUser সব জায়গায় reuse হয়
5. **Clear structure**: কোন endpoint কোথায় আছে সহজে বুঝা যায়

## 📝 বর্তমান Implementation

### ✅ Implemented APIs:

1. **AuthenticationAPI** - 3 endpoints
   - Sign Up
   - Sign In
   - Token Refresh

2. **DashboardAPI** - 2 endpoints
   - Dashboard Insights
   - Search

3. **AIAssistantAPI** - 4 endpoints
   - Tools & Templates
   - Mystery Box
   - Create Thread
   - My Collections

4. **LibraryAPI** - 2 endpoints
   - Library Data
   - Create Collection

5. **HelpAPI** - 2 endpoints
   - Help Articles
   - Contact Us

**Total: 13 endpoints** across 5 API files

## 🎯 পরবর্তী পদক্ষেপ

1. Test run করুন:
   ```bash
   python3 run_tests.py --quick
   ```

2. Specific API test করুন:
   ```bash
   python3 -m locust -f locustfile.py HelpAPI --host=https://backend.amal.education
   ```

3. প্রয়োজন অনুযায়ী নতুন endpoint যোগ করুন

## 💡 Tips

- প্রতিটি API file এ `wait_time = between(1, 3)` দিয়ে request এর মধ্যে delay set করা
- `@task(weight)` দিয়ে কোন endpoint কতবার call হবে তা control করা
- `name="..."` parameter দিয়ে report এ readable name দেখানো
- `catch_response=True` দিয়ে custom success/failure logic লেখা যায়
