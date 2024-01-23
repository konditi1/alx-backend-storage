#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def log_stats():
    # Connect to the MongoDB server
    client = MongoClient('localhost', 27017)

    # Access the 'logs' database and 'nginx' collection
    db = client.logs
    collection = db.nginx

    # Get the total number of documents in the collection
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    # Get the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Get the number of documents with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
