"""
AI Assistant API Load Tests
Tests for tools, templates, threads, and collections
"""
from locust import task, between
from apis.base_user import BaseUser
from faker import Faker

fake = Faker()


class AIAssistantAPI(BaseUser):
    """AI Assistant API test scenarios"""
    
    wait_time = between(1, 3)
    
    def on_start(self):
        """Initialize"""
        super().on_start()
        self.thread_id = None

    @task(2)
    def get_tools_and_templates(self):
        """Test tools and templates endpoint"""
        self.client.get(
            "/api/ai-assistant/tools-and-template/",
            name="AI - Tools & Templates"
        )
    
    @task(2)
    def get_random_mystery_box(self):
        """Test random mystery box endpoint"""
        self.client.get(
            "/api/ai-assistant/random-mystery-box/",
            name="AI - Mystery Box"
        )
    
    @task(1)
    def create_thread(self):
        """Test thread creation"""
        payload = {
            "message": f"Test message - {fake.sentence()}",
            "role": 1  # User role
        }
        
        with self.client.post(
            "/api/ai-assistant/chat/thread/",
            json=payload,
            catch_response=True,
            name="AI - Create Thread"
        ) as response:
            if response.status_code == 200:
                data = response.json()
                self.thread_id = data.get("thread_id")
                response.success()
            else:
                response.failure(f"Thread creation failed: {response.status_code}")
    
    @task(2)
    def get_my_collections(self):
        """Test get my collections"""
        self.client.get(
            "/api/ai-assistant/my-collection/",
            name="AI - My Collections"
        )
