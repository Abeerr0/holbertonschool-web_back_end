#!/usr/bin/env python3
"""102-log_stats.py"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = nginx.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")

    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(nginx.aggregate(pipeline))
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
