#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    logs_collection = client.logs.nginx
    print(f'{logs_collection.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {logs_collection.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {logs_collection.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {logs_collection.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {logs_collection.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {logs_collection.count_documents({"method": "DELETE"})}')
    print(f'{logs_collection.count_documents({"path": "/status"})} status check')
