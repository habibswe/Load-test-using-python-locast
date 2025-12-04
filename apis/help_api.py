from locust import task, between
from apis.base_user import BaseUser

class HelpAPI(BaseUser):
    wait_time = between(1, 2)

    @task
    def get_help_articles(self):
        self.client.get("/api/help-center/help-articles/", name="Help Articles")
