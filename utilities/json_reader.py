import json
import os

class JsonReader:

    def __init__(self, filename):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "test_data", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_data(self, key):
        if isinstance(self.data, list):
            return self.data
        else:
            return self.data.get(key)
