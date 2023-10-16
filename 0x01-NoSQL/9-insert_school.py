#!/usr/bin/env python3

"""
Insert a New School Document into a MongoDB Collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on provided kwargs

    Args:
        mongo_collection: The pymongo collection object
        **kwargs: Keyword arguments representing the fields and values

    Returns:
        The new _id of the inserted document
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
