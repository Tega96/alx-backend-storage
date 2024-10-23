#!/usr/bin/env python3
""" A Python function that returns the list of school having a specific topic """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Return list of schools and topic will be searched """
    if mongo_collection is None:
        return []
    schools = list(mongo_collection.find({"topic": topic }))
    return schools
