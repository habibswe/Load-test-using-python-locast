"""
Base User class for all API tests
Handles authentication and common headers
"""
from locust import HttpUser
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from config.global_login import GLOBAL_TOKEN, API_KEY
except ImportError:
    # Fallback if global_login doesn't exist
    GLOBAL_TOKEN = None
    API_KEY = "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"


class BaseUser(HttpUser):
    """
    Base user class that sets up authentication headers.
    All API test classes should inherit from this.
    """
    
    def on_start(self):
        """Set up headers with authentication"""
        # If global token exists, use it
        if GLOBAL_TOKEN:
            self.client.headers.update({
                "Authorization": f"Bearer {GLOBAL_TOKEN}",
                "X-API-Token": API_KEY,
                "Content-Type": "application/json"
            })
        else:
            # Otherwise, login to get token
            self.login()
    
    def login(self):
        """Login and get access token"""
        headers = {
            "X-API-Token": API_KEY,
            "Content-Type": "application/json"
        }
        
        payload = {
            "username": "mirazhs@proton.me",  # API uses username field for email
            "password": "testing321"
        }
        
        try:
            response = self.client.post(
                "/api/accounts/sign-in/",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                access_token = data.get("access")
                
                # Update headers with token
                self.client.headers.update({
                    "Authorization": f"Bearer {access_token}",
                    "X-API-Token": API_KEY,
                    "Content-Type": "application/json"
                })
            else:
                print(f"Login failed with status code: {response.status_code}")
        except Exception as e:
            print(f"Login error: {e}")
