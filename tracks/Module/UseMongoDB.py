from pymongo import MongoClient
from datetime import datetime
import json
class RecSysLogsToMongo():
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['recSys']
        self.logs = db['logs']

    def insert_log_to_mongodb(self, data):
        data = json.loads(data.decode('utf8'))
        data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.logs.insert_one(data)
        print('Insert data:', data)