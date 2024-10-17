from locust import HttpUser, task

class Pokemon(HttpUser):
    @task
    def list(self):
        # Substitua pelo ip da máquina
        self.client.get("http://host.docker.internal:4444/pokemon") 