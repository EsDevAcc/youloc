# -*- coding: utf-8 -*-
import json
import time
import urllib2
#from pymongo import MongoClient

from django.shortcuts import render, HttpResponse
from business_logic import request_api as ra
from business_logic import mongodb as mngdb
from .tasks import save_data

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Venues
from serializers import VenuesSerializer

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


def index(request):
    request_obj = ra.RequestApi(lat_long="42.6931325,23.3244314", radius=20000)
    url = request_obj.concat_url()
    venues = request_obj.load_json_obj(url)
    context = {'venues': venues}
    return render(request, 'venues/index.html', context)


def saveVenue(request):

    db = mngdb.MongoDB('mytest')
    collection = db.collection('venues')
    data = request.POST

    value = {}
    ids = []
    for key in data:
        if key.startswith('venue'):
            dict_v = {'venue':data[key], 'venueNumber':int(key[5:]), 'date':time.strftime("%Y-%m-%d")}
            result = collection.insert(dict_v)
            if result:
                ids.append(result)

    if ids:
        request_obj = ra.RequestApi(radius=5000)
        url = request_obj.concat_url()
        venues = request_obj.load_json_obj(url)
        save_data(venues, "celery_venue")

    context = {'ids': ids}
    return render(request, 'venues/db_save.html', context)


@api_view(['GET','POST'])
def rest(request):
    db = mngdb.MongoDB('celeryq')
    collection = db.collection('celery_venue')

    venues = []
    if request.method == 'GET':
        for v in enumerate(collection.find()):
            venue = Venues(v[1]["_id"],
                           v[1]["name"],
                           v[1]["contact"],
                           v[1]["location"],
                           v[1]["categories"],
                           int(v[1]["location"]["distance"]),
                           v[1]["verified"],
                           v[1]["stats"],
                           v[1]["url"],
                           v[1]["hours"],
                           v[1]["menu"])
            venues.append(venue)

        serializedList = VenuesSerializer(venues, many=True)
        return Response(serializedList.data)

    elif request.method == 'POST':
        name = request.POST["name"]
        contact = request.POST["contact"]
        location = request.POST["location"]
        category = request.POST["category"]
        distance = request.POST["distance"]
        verified = request.POST["verified"]
        stats = request.POST["stats"]
        url = request.POST["url"]
        hours = request.POST["hours"]
        menu = request.POST["menu"]

        try:
            collection.insert({
                "name": name,
                "contact": contact,
                "location": location,
                "category": category,
                "distance": distance,
                "verified": verified,
                "stats": stats,
                "url": url,
                "hours": hours,
                "menu": menu})
        except:
            return Response({"ok": "false"})
        return Response({"ok": "true"})

    # context = {'venues': venues}
    # return render(request, 'venues/rest.html', context)
