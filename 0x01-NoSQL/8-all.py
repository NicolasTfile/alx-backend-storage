#!/usr/bin/env python3

"""
List All Documents in a MongoDB Collection
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of documents in the collection.
    """
    return mongo_collection.find()
