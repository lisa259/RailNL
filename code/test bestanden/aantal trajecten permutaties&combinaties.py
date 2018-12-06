# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:01:14 2018

@author: My Lenovo
"""

" AANTAL TRAJECTEN BINNEN 120 MINUTEN "

import os
import csv
from itertools import permutations, compress, product 
import timeit

start = timeit.default_timer()

OPDRACHT = "1a"

" IMPORT FILEs "
if OPDRACHT in ["1a", "1b", "1c"]:
    naam_connecties = os.path.join(os.path.dirname(__file__), 'ConnectiesHolland.csv')
    name_stations = os.path.join(os.path.dirname(__file__), 'StationsHolland.csv')
    
bestand_connecties = open(naam_connecties, encoding='utf-8-sig')
all_connections = csv.reader(bestand_connecties)

file_stations = open(name_stations, encoding='utf-8-sig')
all_stations = csv.reader(file_stations)


" CLASSES "
class CONNECTION:
    def __init__(self, station1, station2, duration):
        self.station1 = station1
        self.station2 = station2
        self.duration = duration
        self.critic = False
        self.used = False
    def setCritic(self, critic):
        self.critic = critic
    def setUsed(self, used):
        self.used = used
 
class STATION:
    def __init__(self, name, critic, connections):
        self.name = name
        self.critic = critic
#        self.used = False
        self.connections = connections
        
class TRAJECT:
    def __init__(self):
        self.stations = []
        self.total_time = 0
    def addStation(self, station, index):
        if index == "begin":
            self.stations = [station] + self.stations
        elif index == "end":
            self.stations.append(station)
    def addTotal_time(self, time):
        self.total_time += time

" PUT ALL CONNECTIONS LIKE CONNECTION OBJECT IN LIST "
list_with_connections = []
for connection in all_connections:
    list_with_connections.append(CONNECTION(connection[0], connection[1], int(connection[2])))
    

    
" PUT ALL STATIONS LIKE STATION OBJECT IN LIST "
list_with_stations = []
station_names = []
for station in all_stations:
    if station[-1] == "Kritiek" or OPDRACHT in ["1c"]:
        boolean = True
    else:
        boolean = False

    connections = []
    for conn in list_with_connections:
        if station[0] == conn.station1 or station[0] == conn.station2:
            connections.append(conn)
            if boolean:
                conn.setCritic(boolean)
    list_with_stations.append(STATION(station[0], boolean, connections))
    station_names.append(station[0])
     
#for i in permutations(station_names):
#    print(i)

def combination(items):
    return(set(compress(items, mask)) for mask in product(*[[0,1]]*len(items)))    

for i in combination(station_names):
    print(i)
    
stop = timeit.default_timer()

print('Time in minutes: ', (stop-start)/60)  