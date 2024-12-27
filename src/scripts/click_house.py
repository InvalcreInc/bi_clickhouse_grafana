from clickhouse_driver import Client
from clickhouse_connect import get_client
import json
import os
import csv
import pandas as pd


class IDS:
    def __init__(self):
        self.x = 0

    def load_data(self, filepath) -> list:
        script_dir = os.path.dirname(__file__)
        filepath = os.path.join(script_dir, filepath)
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data[1:]


class ClickHouse:
    '''
    ClickHouse class to perform clickhouse queries

    '''

    def __init__(self):
        self.client = get_client(host='localhost')

    def create_table(self):
        '''
        Create a clickhouse table if it does not exist.
        '''
        query = '''
        CREATE TABLE IF NOT EXISTS idsdb.labelled_testing_data(
            timestamp Float64,
            processId UInt64,
            threadId UInt64,
            parentProcessId UInt64,
            userId UInt64,
            mountNamespace UInt64,
            processName String,
            hostName String,
            eventName String,
            stackAddresses Array(UInt64),
            evil UInt64,
            )
            ENGINE = MergeTree() ORDER BY timestamp
        '''
        try:
            self.client.command(query)
        except Exception as e:
            print(e)

    def insert(self, data):
        '''
        Insert data into clickhouse db.
        '''
        try:
            data['args'] = [json.dumps(arg) for arg in data['args']]
            self.client.insert('ids.labelled_testing_data', data)
        except Exception as e:
            print(e)


ids = IDS()
data = ids.load_data('../data/labelled_testing_data.csv')
print(data[:2])
clickhouse = ClickHouse()
clickhouse.create_table()
clickhouse.insert(data)
# todo
