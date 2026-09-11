#!/usr/bin/env python3
"""Module that inserts a new document in a collection based on kwargs"""

def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    return list(mongo_collection.find({"topics": topic}))