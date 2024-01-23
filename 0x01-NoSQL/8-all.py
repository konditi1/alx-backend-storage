#!/usr/bin/env python3
"""
 function that lists all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """
    lists all documents in a collection
    :param mongo_collection:
    :return:list of documents
    """
    if mongo_collection is None:
        return []
    return [doc for doc in mongo_collection.find()]
