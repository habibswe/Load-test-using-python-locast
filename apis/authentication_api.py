"""
Authentication API Load Tests
Tests for sign up, sign in, and token refresh
"""
from locust import task, between
from apis.base_user import BaseUser
from faker import Faker

fake = Faker()


class AuthenticationAPI(BaseUser):
    """Authentication API test scenarios"""
    
    wait_time = between(1, 3)
    
    def on_start(self):
        """Initialize test data"""
        self.test_email = fake.email()
        self.test_password = "testing321"
        self.access_token = None
        self.refresh_token = None
        # Don't call parent on_start to avoid auto-login

    @task(1)
    def sign_up(self):
        """Test user registration"""
        payload = {
            "email": self.test_email,
            "password": self.test_password
        }
        
        headers = {
            "X-API-Token": "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d",
            "Content-Type": "application/json"
        }
        
        with self.client.post(
            "/api/accounts/sign-up/",
            json=payload,
            headers=headers,
            catch_response=True,
            name="Auth - Sign Up"
        ) as response:
            if response.status_code == 201:
                data = response.json()
                self.access_token = data.get("access")
                self.refresh_token = data.get("refresh")
                response.success()
            elif response.status_code == 409:
                # User already exists
                response.success()
            else:
                response.failure(f"Sign up failed: {response.status_code}")
    
    @task(2)
    def sign_in(self):
        """Test user login"""
        payload = {
            "username": "mirazhs@proton.me",  # API uses username field for email
            "password": "testing321"
        }
        
        headers = {
            "X-API-Token": "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d",
            "Content-Type": "application/json"
        }
        
        with self.client.post(
            "/api/accounts/sign-in/",
            json=payload,
            headers=headers,
            catch_response=True,
            name="Auth - Sign In"
        ) as response:
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get("access")
                self.refresh_token = data.get("refresh")
                response.success()
            else:
                response.failure(f"Sign in failed: {response.status_code}")
    
    @task(1)
    def refresh_token(self):
        """Test token refresh"""
        if not self.refresh_token:
            return
        
        payload = {
            "refresh": self.refresh_token
        }
        
        headers = {
            "X-API-Token": "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d",
            "Content-Type": "application/json"
        }
        
        with self.client.post(
            "/api/accounts/token/refresh/",
            json=payload,
            headers=headers,
            catch_response=True,
            name="Auth - Token Refresh"
        ) as response:
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get("access")
                self.refresh_token = data.get("refresh")
                response.success()
            else:
                response.failure(f"Token refresh failed: {response.status_code}")
