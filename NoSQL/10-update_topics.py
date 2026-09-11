#!/usr/bin/env python3
"""Module that inserts a new document in a collection based on kwargs"""

def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document based on the name"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )