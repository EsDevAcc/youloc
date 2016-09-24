from __future__ import absolute_import

from celery import shared_task
from pymongo import MongoClient
from business_logic import mongodb as mngdb

@shared_task
def save_data(obj, colection_name):

    db = mngdb.MongoDB('celeryq')
    collection = db.collection(colection_name)
    for item in obj:
        collection.insert(item)


