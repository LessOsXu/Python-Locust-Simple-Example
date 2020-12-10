import time
from locust import HttpUser, task, between

"""
The locust version 1.4.1 as below:
"""


class QuickstartUser(HttpUser):
    # The class defines a wait_time that will make the simulated users wait
    # between 1 and 2.5 seconds after each task.
    wait_time = between(1, 2.5)

    # @task(7) mean this method have 70% rate to be executed.
    @task(7)
    def hello_world(self):
        self.client.get('/login', verify=False)
        body = {
            'username': 'oscar',
            'password': '123456',
            'next': '/',
        }
        with self.client.post('/login', data=body, verify=False) as response:
            if b"DDDDD" not in response.content:
                self.client.request_success()
            else:
                self.client.request_failure()

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id=c", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.get("/")
