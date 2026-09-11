#!/usr/bin/env python3
"""Script that provides stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('127.0.0.1', 27017)
    nginx_collection = client.logs.nginx

    # 1. Total logs
    n_logs = nginx_collection.count_documents({})
    print(f"{n_logs} logs")

    # 2. Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
