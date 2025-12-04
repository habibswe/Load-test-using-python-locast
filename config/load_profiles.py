from locust import LoadTestShape

class HeavyLoad(LoadTestShape):
    """
    Profile for stress test
    """
    stages = [
        {"duration": 60, "users": 50, "spawn_rate": 5},
        {"duration": 120, "users": 100, "spawn_rate": 10},
        {"duration": 180, "users": 200, "spawn_rate": 20},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])

        return None
