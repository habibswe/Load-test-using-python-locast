"""
Main Locustfile - Load Testing with One-Time Login
This file coordinates multiple API tests with a single global login.
"""

from locust import HttpUser, task, between
from locust.exception import StopUser

# Import global login to ensure it runs
import config.global_login

class MultiAPIUser(HttpUser):
    """
    Main user class that runs multiple APIs concurrently.
    Login happens once globally before all tests start.
    Each user will randomly execute tasks from all APIs.
    """
    wait_time = between(1, 3)
    
    def on_start(self):
        """
        Called when a simulated user starts.
        Headers are set with the global token from one-time login.
        """
        token = config.global_login.GLOBAL_TOKEN
        api_key = config.global_login.API_KEY
        
        self.client.headers.update({
            "Authorization": f"Bearer {token}",
            "X-API-Token": api_key,
            "Content-Type": "application/json"
        })
        print(f"User started with global token: {token[:30] if token else 'None'}...")
    
    # Dashboard API Tasks (DISABLED)
    # @task(3)  # Weight: 3 (runs more frequently)
    # def get_dashboard(self):
    #     """Get dashboard data"""
    #     self.client.get("/api/dashboard/", name="Dashboard")
    
    # @task(2)  # Weight: 2
    # def get_user_profile(self):
    #     """Get user profile"""
    #     self.client.get("/api/user/profile/", name="User Profile")
    
    # Help API Tasks
    @task(2)  # Weight: 2
    def get_help_articles(self):
        """Get help center articles"""
        self.client.get("/api/help-center/help-articles/", name="Help Articles")
        # Stop the user after one run
        raise StopUser()
    
    # PDF API Tasks (DISABLED)
    # @task(1)  # Weight: 1 (runs less frequently - more resource intensive)
    # def generate_pdf(self):
    #     """Generate PDF document"""
    #     payload = {
    #         "html": "<h1>Test PDF</h1>",
    #         "title": "PDF Example",
    #         "landscape": True
    #     }
    #     self.client.post("/api/generate-pdf", json=payload, name="PDF Generate")
