#!/usr/bin/env python3
""" Inserts A New Document In A Collection Based On kwargs """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs:
        param mongo_collection: pymongo collection object
        param kwargs: keyword arguments representing the data to insert
        return: the new _id
    """
    new_school_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_school_id
