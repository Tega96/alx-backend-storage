#!/usr/bin/env python3
""" A python function that changes al topics of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """" name(string) will be the school name to update, topics(list of string) """
    if mongo_collection is None:
        return []
    topic_change = mongo_collection.update(
            { "name": name },
            {"$set": {"topics" : topics }},
            )
    return topic_change
