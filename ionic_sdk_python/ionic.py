import requests


class Ionic:
    # PROD_SERVER = "https://ionic-commerce-server.fly.dev"
    PROD_SERVER = "https://api.ionicapi.com"

    def __init__(self, server_url=None):
        self.server_url = server_url or self.PROD_SERVER

    def query(self, query):
        url = f"{self.server_url}/query"
        payload = {"query": f"{query}"}
        result = requests.post(url, json=payload)

        return result.json()
