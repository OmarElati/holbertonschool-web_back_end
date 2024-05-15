#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client =MongoClient('mongodb://localhost:27017/')
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    status_check = logs_collection.count_documents({"path": "/status"})
    print (f"{status_check} status check")
