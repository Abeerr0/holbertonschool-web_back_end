#!/usr/bin/env python3
"""Script that provides stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

if __name__ == "__main__":
    try:
        client = MongoClient('127.0.0.1', 27017, serverSelectionTimeoutMS=2000)
        # اختبار الاتصال
        client.admin.command('ping')

        nginx_collection = client.logs.nginx
        n_logs = nginx_collection.count_documents({})
        print(f"{n_logs} logs")

        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            count = nginx_collection.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")

        status_check = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
        )
        print(f"{status_check} status check")

    except ConnectionFailure:
        print("خطأ: قاعدة البيانات MongoDB غير شغالة على جهازك المحلي حالياً.")