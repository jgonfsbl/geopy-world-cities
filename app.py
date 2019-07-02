# -*- coding: utf-8 -*-

""" GeoPy test """

__author__ = 'ea1het'


from geopy import distance
import json
import time

MADRID = (40.4168, -3.7038)
NUM = 10

start = time.time()

with open('cities.json') as ciudades:
    data = json.load(ciudades)

i = 0
for p in data:
    print('\nCiudad: ' + p['name'])
    print('Distancia a MADRID: %.2f km' % distance.distance(MADRID, (p['lat'], p['lng'])).km)
    i += 1

end = time.time()

print('\nEvaluadas un total de %s ciudades en %s segundos' % (i, round((end-start),2)))
