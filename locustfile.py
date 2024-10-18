from locust import HttpUser, task
# from generate_pokemons import get_random

class Pokemon(HttpUser):    
    @task
    def list(self):
        # Endereço da API no docker
        self.client.get("http://node-api:4444/pokemon")