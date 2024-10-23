#!/usr/bin/env python3
""" A function that inserts a new document in a collection based on kwargs """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ insert a new document in collection and return the id"""
    if mongo_collection is None:
        return []
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
