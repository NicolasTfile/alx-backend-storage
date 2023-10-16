#!/usr/bin/env python3

"""
Return the List of Schools with a Specific Topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools that have a specific topic

    Args:
        mongo_collection: The pymongo collection object
        topic (str): The topic to search for

    Returns:
        A list of schools with the specified topic
    """
    return mongo_collection.find({"topics": topic})
