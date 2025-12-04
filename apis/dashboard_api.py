# from locust import task, between
# from apis.base_user import BaseUser

# class DashboardAPI(BaseUser):
#     wait_time = between(1, 3)

#     @task
#     def get_dashboard(self):
#         self.client.get("/api/dashboard/", name="Dashboard")
    
#     @task
#     def get_user_profile(self):
#         self.client.get("/api/user/profile/", name="User Profile")
