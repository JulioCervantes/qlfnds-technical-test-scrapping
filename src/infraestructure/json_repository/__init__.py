import json
import os
import requests


class JsonRepository:
    def load_json(self, origin):
        if origin.startswith("http://") or origin.startswith("https://"):
            return self.load_json_from_url(origin)
        else:
            return self.load_json_from_file(origin)

    @staticmethod
    def load_json_from_file(path):
        if not os.path.isfile(path):
            raise ValueError("File not found")
        with open(path) as f:
            return json.load(f)

    @staticmethod
    def load_json_from_url(url):
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("URL not found")
        return response.json()