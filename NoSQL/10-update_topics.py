#!/usr/bin/env python3
""" Changes All Topics Of A School Document Based On The Name """


def update_topics(mongo_collection, name, topics):
    """
    Changes All Topics Of A School Document Based On The Name:
        param mongo_collection: pymongo collection object
        param name: school name to update
        param topics: list of topics approached in the school
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
