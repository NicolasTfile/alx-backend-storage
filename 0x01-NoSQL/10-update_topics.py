#!/usr/bin/env python3

"""
Update Topics of a School Document in a MongoDB Collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the school's name

    Args:
        mongo_collection: The pymongo collection object
        name (str): The name of the school to update
        topics (list of str): The list of topics to set for the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
