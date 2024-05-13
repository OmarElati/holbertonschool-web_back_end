#!/usr/bin/env python3
""" List All Docuements In A Collection """


def list_all(mongo_collection):
    """ List All Docuements In A Collection """
    return mongo_collection.find()
