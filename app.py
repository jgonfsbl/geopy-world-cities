# -*- coding: utf-8 -*-

""" GeoPy test """

__author__ = 'ea1het'


from geopy import distance
import json

MADRID = (40.4168, -3.7038)

with open('cities.json') as ciudades:
    data = json.load(ciudades)

    for p in data:
        print('\nCiudad: ' + p['name'])
        print('Distancia a MADRID: %.2f km' % distance.distance(MADRID, (p['lat'], p['lng'])).km)
