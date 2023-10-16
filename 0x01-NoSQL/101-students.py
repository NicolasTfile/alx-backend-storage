#!/usr/bin/env python3

"""
This script defines a function to retrieve and sort student data
from a MongoDB collection based on their average scores
"""


def top_students(mongo_collection):
    """
    Retrieve and sort students by their average score

    Args:
        mongo_collection: Pymongo collection object containing student data

    Returns:
        A list of students sorted in descending order by their average score
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])
