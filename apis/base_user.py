from locust import HttpUser
from config.global_login import GLOBAL_TOKEN, API_KEY

class BaseUser(HttpUser):
    """
    Base user class that sets up authentication headers.
    All API test classes should inherit from this.
    """
    
    def on_start(self):
        """Set up headers with global token from one-time login"""
        self.client.headers.update({
            "Authorization": f"Bearer {GLOBAL_TOKEN}",
            "x-api-key": API_KEY,
            "Content-Type": "application/json"
        })

