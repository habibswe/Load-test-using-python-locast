"""
Library API Load Tests
Tests for library data and collection management
"""
from locust import task, between
from apis.base_user import BaseUser
from faker import Faker
import random

fake = Faker()


class LibraryAPI(BaseUser):
    """Library API test scenarios"""
    
    wait_time = between(1, 3)
    
    def on_start(self):
        """Initialize"""
        super().on_start()
        self.collection_id = None

    @task(2)
    def get_library_data(self):
        """Test library data retrieval"""
        self.client.get(
            "/api/ai-assistant/library/",
            name="Library - Get Data"
        )
    
    @task(1)
    def create_collection(self):
        """Test collection creation"""
        payload = {
            "title": f"Load Test Collection - {fake.word()}",
            "description": fake.sentence(),
            "privacy": random.choice([1, 2]),  # 1=Private, 2=Public
            "color_code": random.choice(["#FF5733", "#33FF57", "#3357FF", "#F333FF"])
        }
        
        with self.client.post(
            "/api/ai-assistant/create-collection/",
            json=payload,
            catch_response=True,
            name="Library - Create Collection"
        ) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f"Collection creation failed: {response.status_code}")
