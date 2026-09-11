#!/usr/bin/env python3
"""Function that returns all students sorted by average score."""


def top_students(mongo_collection):
    """Return all students sorted by average score."""
    students = list(mongo_collection.find())

    for student in students:
        topics = student.get("topics", [])
        if topics:
            total = sum(topic.get("score", 0) for topic in topics)
            student["averageScore"] = total / len(topics)
        else:
            student["averageScore"] = 0

    return sorted(
        students,
        key=lambda student: student["averageScore"],
        reverse=True
    )