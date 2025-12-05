"""
Dashboard API Load Tests
Tests for dashboard and search endpoints
"""
from locust import task, between
from apis.base_user import BaseUser


class DashboardAPI(BaseUser):
    """Dashboard API test scenarios"""
    
    wait_time = between(1, 3)

    @task(3)
    def get_dashboard_insights(self):
        """Test dashboard daily insights"""
        self.client.get(
            "/api/dashboard/",
            name="Dashboard - Daily Insights"
        )
    
    @task(2)
    def search_anything(self):
        """Test search functionality"""
        import random
        search_queries = ["", "a", "test", "chat", "collection"]
        query = random.choice(search_queries)
        
        self.client.get(
            f"/api/dashboard/v2/search/?q={query}",
            name="Dashboard - Search"
        )
