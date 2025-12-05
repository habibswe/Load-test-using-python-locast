"""
Help Center API Load Tests
Tests for help articles and contact form
"""
from locust import task, between
from apis.base_user import BaseUser
from faker import Faker

fake = Faker()


class HelpAPI(BaseUser):
    """Help Center API test scenarios"""
    
    wait_time = between(1, 2)

    @task(2)
    def get_help_articles(self):
        """Test help articles listing"""
        self.client.get(
            "/api/help-center/help-articles/",
            name="Help - Articles List"
        )
    
    @task(1)
    def submit_contact_us(self):
        """Test contact us form submission"""
        payload = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone_number": fake.phone_number()[:11],
            "message": fake.text(max_nb_chars=200)
        }
        
        self.client.post(
            "/api/help-center/contact-us/",
            json=payload,
            name="Help - Contact Us"
        )
