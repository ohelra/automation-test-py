import pandas as pd
import os

class ExcelReader:

    def __init__(self, file_name):
        self.file_path = os.path.join(os.getcwd(), 'test_data', file_name)

    def get_zipcode_data(self):
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"Not found file: {self.file_path}")

            if self.file_path.endswith(".csv"):
                df = pd.read_csv(self.file_path,   dtype={'PHYSICAL ZIP' : str})
            else:
                df = pd.read_excel(self.file_path, dtype={'PHYSICAL ZIP' : str})

            df = df.fillna("")
            return df[['PHYSICAL ZIP', 'PHYSICAL CITY', 'STATE']].to_dict('records')

        except Exception as e:
            print(f"Error : {e}")
            return []
