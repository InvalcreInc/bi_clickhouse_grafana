import pandas as pd
import json
import os

class CSVData:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        data = pd.read_csv(self.filepath)
        return data

    def stringfy_column(self, column):
        column = column.replace("'", "\"")
        columns = json.loads(column)
        stringfied = [json.dumps(x) for x in columns]
        return stringfied

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, '../data/labelled_testing_data.csv')
    csv_data = CSVData(filepath)
    data = csv_data.load_data()
    data= data.drop(columns=['args'])
    print(data[:2])
    data.to_csv(filepath, index=False)
