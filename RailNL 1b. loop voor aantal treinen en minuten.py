# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:35:43 2018

@author: My Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:26:50 2018

@author: My Lenovo
"""
import os
import xlrd
import math

" IMPORT CONNECTIES FILE "
naam_connecties = os.path.join(os.path.dirname(__file__), 'ConnectiesHolland.xlsx')
bestand_connecties = xlrd.open_workbook(naam_connecties)
sheet1_connecties = bestand_connecties.sheet_by_index(0)
nrows1_connecties = sheet1_connecties.nrows

" IMPORT STATIONS FILE "
name_stations = os.path.join(os.path.dirname(__file__), 'StationsHolland.xlsx')
file_stations = xlrd.open_workbook(name_stations)
sheet1_stations = file_stations.sheet_by_index(0)
nrows1_stations = sheet1_stations.nrows

" CLASSES "
class CONNECTION:
    def __init__(self, station1, station2, duration):
        self.station1 = station1
        self.station2 = station2
        self.duration = duration
        self.critic = False # SET TRUE VOOR ALLES KRITIEK
        self.used = False
    def setCritic(self, critic):
        self.critic = critic # SET TRUE VOOR ALLES KRITIEK
    def setUsed(self, used):
        self.used = used
 
class STATION:
    def __init__(self, name, critic, connections):
        self.name = name
        self.critic = critic # SET TRUE VOOR ALLES KRITIEK
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
    # zoeken naar korste ongebruikte kritieke spoor
    for conn in list_with_connections:
        if conn.critic == True and conn.used == False and conn.duration < minimum:
            minimum = conn.duration
            shortest = conn
    # spoor gevonden: nieuw traject van maken
    if shortest != None:
        new = TRAJECT()
        new.addStation(shortest.station1, "end")
        new.addStation(shortest.station2, "end")
        new.addTotal_time(minimum)
        shortest.setUsed(True)
        return new
    # geen spoor gevonden
    return False

"KORTSTE ONGEBRUIKTE KRITIEKE PAD ZOEKEN + TOEVOEGEN AAN TRAJECT"
def new_connection(station1, station2, traject):
    minimum = math.inf
    shortest = None
    # zoekt kortste, ongebruikte, kritiek spoore, dat aansluit op station1 of station2
    for conn in list_with_connections:
        if conn.critic == True and conn.used == False and conn.duration < minimum and (conn.station1 == station1 or conn.station1 == station2 or conn.station2 == station1 or conn.station2 == station2):
            minimum = conn.duration
            shortest = conn
    # spoor gevonden en valt nog binnen de tijd: toevoegen aan traject
    if shortest != None and traject.total_time + minimum <= MAX_AANTAL_MINUTEN:
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
    # geen spoor gevonden om toe te kunnen voegen
    return False
    
" ALGORITME VAN DIJKSTRA "          
def Dijkstra(current):
    # maak dictionary van onbezochte stations met afstand vanaf beginpunt. zet afstand nu op infinity
    unvisited = {station.name: math.inf for station in list_with_stations}
    visited = {}
    currentDistance = 0
    # set de afstand van current (begin) station op 0
    unvisited[current] = currentDistance
    #dictionary die opslaat wat de voorganger van een station is
    parents = {}
        
    #bepaal korste afstand van beginstation naar alle andere stations
    while True:
        for station in list_with_stations:
            if current == station.name:
                # alle connecties van huidig station afgaan
                for connectie in station.connections:
                    # sla aansluitend station op als neighbour
                    if current == connectie.station1:
                        neighbour = connectie.station2
                    elif current == connectie.station2:
                        neighbour = connectie.station1
                    if neighbour not in unvisited: continue
                
                    
                    newDistance = currentDistance + connectie.duration
                    
                    if unvisited[neighbour] > newDistance:
                        unvisited[neighbour] = newDistance
                        # add neighbour en current als link toe aan dictionary
                        parents[neighbour] = current
                        
        # sla current station op als bezocht en verwijder uit onbezocht      
        visited[current] = currentDistance
        del unvisited[current]
        
        # geen onbezochte stations meer over
        if not unvisited: break
        
        # lijst met (neighbour, afstand)
        candidates = [node for node in unvisited.items() if node[1]]
        # neemt station met korste afstand als nieuwe current
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return [visited, parents]

" PATH VAN DIJKSTRA OPSTELLEN: VAN GEVRAAGD NAAR BEGIN STATION "
def _deconstruct_path(parents, end):
    if end not in parents:
        # geen path mogelijk
        return None
    
    gezocht = end
    path = []
    while gezocht:
        path.append(gezocht)
        # set gezocht op voorgaande station van huidig gezocht
        gezocht = parents.get(gezocht)
    return path

" ONGEBRUIKTE KRITIEKE SPOREN TOEVOEGEN AAN BESTAANDE TRAJECTEN "
def linken(stations, time):
    #stations bevat de 2 stations van de ongebruikte connectie
    minimum = math.inf
    
    for add_station in stations:
        # dijkstra returnt een dictionary met stations + korste afstand naar dit station en een dictionary met stations + voorgegaande station
        dijkstra = Dijkstra(add_station)
        verbindingen = dijkstra[0]
        parents = dijkstra[1]
       
        for station, afstand in verbindingen.items():
            for traject in list_with_trajects:
                # check of station aansluit op het traject, en of de afstand minimaal is, en of het de totale aantal min van het traject niet overstrijd
                if (station == traject.stations[0] or station == traject.stations[-1]) and afstand < minimum and traject.total_time + afstand + time <= MAX_AANTAL_MINUTEN and afstand != 0:
                    minimum = afstand
                    end = station
                    in_traject = traject
                    safe_parents = parents
                    if add_station == stations[0]:
                        toevoegen = stations[1]
                    else:
                        toevoegen = stations[0]
     
    # aansluitend traject gevonden: connectie toevoegen aan best aansluitende traject            
    if minimum != math.inf:
        # haal het korste pad op van beginstation naar aansluitend station (uit traject)
        path = _deconstruct_path(safe_parents, end)
        if end == in_traject.stations[0]:
            plek = "begin"
        elif end == in_traject.stations[-1]:
            plek = "end"
        if path != None:  
            in_traject.addTotal_time(minimum + time)
            # path toevoegen aan traject
            for index in range(1, len(path)):
                in_traject.addStation(path[index], plek)
            # andere station uit connectie ook toevoegen
            in_traject.addStation(toevoegen, plek)
            return True
    return False
 
" BEPALEN KWALITEIT VAN LIJNVOERING "       
def doelfunctie():
    # bepalen p
    aantalkritiek = 0
    aantalgebruikt = 0
    for connection in list_with_connections:
        if connection.critic:
            aantalkritiek += 1
            if connection.used:
                aantalgebruikt += 1
    p = aantalgebruikt / aantalkritiek
    
    T = len(list_with_trajects)
    
    # bepalen Min
    Min = 0
    for traject in list_with_trajects:
        Min += traject.total_time
    
    return (p * 10000 - T * 20 - Min / 10)

tot = []
maxdoel = 0
for gfd in range(1, 8):
    for tyu in range(120, 0, -1):
        " RESTRICTIES LIJNVOERING "
        MAX_AANTAL_TREINEN = gfd
        MAX_AANTAL_MINUTEN = tyu
        
        
        " PUT ALL CONNECTIONS LIKE CONNECTION OBJECT IN LIST "
        list_with_connections = []
        for i in range(0, nrows1_connecties):
            # van ['plaats1, plaats2, afstand'] naar ["plaats1", "plaats2", "afstand"] 
            splitted = sheet1_connecties.row_values(i)[0].split(',')
            
            list_with_connections.append(CONNECTION(splitted[0], splitted[1], int(splitted[2])))
            
        
            
        " PUT ALL STATIONS LIKE STATION OBJECT IN LIST "
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
               
        " CREATE X AMOUNT OF TRAJECTS "
        list_with_trajects = []  
        while len(list_with_trajects) < MAX_AANTAL_TREINEN:
            # aanroepen functie new_traject voor opstellen traject
            new = new_traject()
            if new != False:
                list_with_trajects.append(new)
            
            # aanroepen functie new_connection voor uitbreiden traject
            while True:
                new = new_connection(list_with_trajects[-1].stations[0], list_with_trajects[-1].stations[-1], list_with_trajects[-1])
                if new == False:
                    break
                list_with_trajects[-1] = new
                
        " TRY TO ADD UNUSED CRITIC CONNECTIONS TO EXISTING TRAJECTS "
        for i in list_with_connections:   
            if i.used == False and i.critic == True:
                if linken([i.station1, i.station2], i.duration):
                    i.setUsed(True)
                            
                               
#        " PRINT FINAL TRAJECTS "                   
#        print("___________TRAJECTEN:___________")
#        for traject in list_with_trajects:
#            print(traject.stations)
#            print(traject.total_time)
#            print("")
#        
        
        " PRINT UNUSED CONNECTIONS " 
        aantal = 0
        for i in list_with_connections: 
            if i.used == False and i.critic == True:    
                aantal += 1
#                print(i.station1 + " - " + i.station2 + "  worden niet gebruikt")
        doel = doelfunctie()
        tot.append([gfd, tyu, doel, aantal])
#        print(doelfunctie())
        if doel >= maxdoel:
            maxdoel = doel
            trei = gfd
            minu = tyu
            aant = aantal
        
print(tot)
print("")
print(maxdoel)
print(trei)
print(minu)
print(aant)