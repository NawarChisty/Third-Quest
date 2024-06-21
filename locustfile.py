from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    
    @task(1)
    def load_test(self):
        with self.client.get("/data?page=1&limit=10", catch_response=True) as response:
            if response.elapsed.total_seconds() > 1:
                response.failure("Response time exceeded 1 second")
            else:
                response.success()

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)
