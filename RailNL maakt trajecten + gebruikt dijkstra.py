# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:26:50 2018

@author: My Lenovo
"""
import os
import xlrd
import math

""" IMPORT CONNECTIES FILE """
naam_connecties = os.path.join(os.path.dirname(__file__), 'ConnectiesHolland.xlsx')
bestand_connecties = xlrd.open_workbook(naam_connecties)
sheet1_connecties = bestand_connecties.sheet_by_index(0)
nrows1_connecties = sheet1_connecties.nrows

""" IMPORT STATIONS FILE """
name_stations = os.path.join(os.path.dirname(__file__), 'StationsHolland.xlsx')
file_stations = xlrd.open_workbook(name_stations)
sheet1_stations = file_stations.sheet_by_index(0)
nrows1_stations = sheet1_stations.nrows

""""CLASSES """
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
            
        

"NIEUW TRAJECT"
def new_traject():
    minimum = math.inf
    shortest = None
    for conn in list_with_connections:
        if conn.critic == True and conn.used == False and conn.duration < minimum:
            minimum = conn.duration
            shortest = conn
    if shortest != None:
        new = TRAJECT()
        new.addStation(shortest.station1, "end")
        new.addStation(shortest.station2, "end")
        new.addTotal_time(minimum)
        shortest.setUsed(True)
        return new
    else:
        return False

"KORTSTE ONGEBRUIKTE KRITIEKE PAD ZOEKEN"
def new_connection(station1, station2, traject):
    minimum = math.inf
    shortest = None
    for conn in list_with_connections:
        if conn.critic == True and conn.used == False and conn.duration < minimum and (conn.station1 == station1 or conn.station1 == station2 or conn.station2 == station1 or conn.station2 == station2):
            minimum = conn.duration
            shortest = conn
    if shortest != None and traject.total_time + minimum <= 120:
        if station1 == shortest.station1:
            traject.addStation(shortest.station2, "begin")
        elif station1 == shortest.station2:
            traject.addStation(shortest.station1, "begin")
        elif station2 == shortest.station1:
            traject.addStation(shortest.station2, "end")
        elif station2 == shortest.station2:
            traject.addStation(shortest.station1, "end")
        traject.addTotal_time(minimum)
        shortest.setUsed(True)
        return traject
    else:
        return False
    
            
def Dijkstra(current):
    unvisited = {node.name: math.inf for node in list_with_stations} #using None as +inf
    visited = {}
    currentDistance = 0
    unvisited[current] = currentDistance
    parents = {}
    
    while True:
        for station in list_with_stations:
            if current == station.name:
                for connectie in station.connections:
                    if current == connectie.station1:
                        neighbour = connectie.station2
                    elif current == connectie.station2:
                        neighbour = connectie.station1
                    if neighbour not in unvisited: continue
                    newDistance = currentDistance + connectie.duration
                    if (unvisited[neighbour] == math.inf or unvisited[neighbour] > newDistance):
                        unvisited[neighbour] = newDistance
                        parents[neighbour] = current
                
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return [visited, parents]

def _deconstruct_path(tentative_parents, end):
    if end not in tentative_parents:
        return None
    cursor = end
    path = []
    while cursor:
        path.append(cursor)
        cursor = tentative_parents.get(cursor)
    return path

def linken(stations):
    minimum = math.inf
    
    for add_station in stations:
        dijkstra = Dijkstra(add_station)
        lijst = dijkstra[0]
        parents = dijkstra[1]
       
        for station, afstand in lijst.items():
            for traject in list_with_trajects:
                if (station == traject.stations[0] or station == traject.stations[-1]) and afstand < minimum and traject.total_time + afstand <= 120:
                    minimum = afstand
                    end = station
                    in_traject = traject
                    safe_parents = parents
                    if add_station == stations[0]:
                        toevoegen = stations[1]
                    else:
                        toevoegen = stations[0]
                    
    if minimum != math.inf:
        path = _deconstruct_path(safe_parents, end)
        if end == in_traject.stations[0]:
            plek = "begin"
        elif end == in_traject.stations[-1]:
            plek = "end"
        if path != None:  
            in_traject.addTotal_time(minimum)
            for index in range(1, len(path)):
                in_traject.addStation(path[index], plek)
            in_traject.addStation(toevoegen, plek)
            return True
    return False
        
def doelfunctie():
    aantalkritiek = 0
    aantalgebruikt = 0
    for connection in list_with_connections:
        if connection.critic:
            aantalkritiek += 1
            if connection.used:
                aantalgebruikt += 1
    p = aantalgebruikt / aantalkritiek
    
    T = len(list_with_trajects)
    
    Min = 0
    for traject in list_with_trajects:
        Min += traject.total_time
        
    return (p * 10000 - T * 20 - Min / 10)


""" PUT ALL CONNECTIONS LIKE CONNECTION OBJECT IN LIST """
list_with_connections = []
for i in range(0, nrows1_connecties):
    # van ['plaats1, plaats2, afstand'] naar ["plaats1", "plaats2", "afstand"] 
    splitted = sheet1_connecties.row_values(i)[0].split(',')
    
    list_with_connections.append(CONNECTION(splitted[0], splitted[1], int(splitted[2])))
    

    
""" PUT ALL STATIONS LIKE STATION OBJECT IN LIST"""
list_with_stations = []
for i in range(0, nrows1_stations):
    # van ['station, x, y, (Kritiek)'] naar ["station", "x", "y", "(Kritiek)"]
    splitted = sheet1_stations.row_values(i)[0].split(',')
    
    if splitted[-1] == "Kritiek":
        boolean = True
    else:
        boolean = False

    connections = []
    for conn in list_with_connections:
        if splitted[0] == conn.station1 or splitted[0] == conn.station2:
            connections.append(conn)
            if boolean == True:
                conn.setCritic(boolean)
    list_with_stations.append(STATION(splitted[0], boolean, connections))
       


list_with_trajects = []
    
while len(list_with_trajects) < 7:
    new = new_traject()
    if new != False:
        list_with_trajects.append(new)
    go = True
    while go == True:
        new = new_connection(list_with_trajects[-1].stations[0], list_with_trajects[-1].stations[-1], list_with_trajects[-1])
        if new != False:
            list_with_trajects[-1] = new
        else:
            go = False

for i in list_with_connections:   
    if i.used == False and i.critic == True:
        if linken([i.station1, i.station2]):
            i.setUsed(True)
                    
                
        
                    
print("___________TRAJECTEN:___________")
for traject in list_with_trajects:
    print(traject.stations)
    print(traject.total_time)
    print("")
       
for i in list_with_connections:   
  if i.used == False and i.critic == True:     
      print(i.station1 + " - " + i.station2 + "  worden niet gebruikt")
      
print(doelfunctie())