#!/usr/bin/env python3
""" List Of School Having A Specific Topic """


def schools_by_topic(mongo_collection, topic):
    """
    List Of School Having A Specific Topic:
        Param mongo_collection: pymongo collection object
        Param topic: topic to search for
    """
    return mongo_collection.find({"topic": topic})
