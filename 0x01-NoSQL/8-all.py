#!/usr/bin/env python3
""" A function that lists all documents in a collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ Return an empty list if no document in a collection """
    if mongo_collection is None:
        return []
    doc = list(mongo_collection.find())
    return doc
