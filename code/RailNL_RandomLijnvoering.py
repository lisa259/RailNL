from classes.class_CONNECTION import CONNECTION
from classes.class_TRAJECT import TRAJECT
from functies.def_importeren import importeren
from StateSpace import statespace
from functies.def_doelfunctie import doelfunctie
import random

exportfile = open('export_statespace_random.csv', 'a') 

OPDRACHT = "1d"

bestanden = importeren(OPDRACHT)
all_connections = bestanden[0]
all_stations = bestanden[1]

list_with_connections = []
for connection in all_connections:
    list_with_connections.append(CONNECTION(connection[0], connection[1], float(connection[2])))

for station in all_stations:
    if station[-1] == "Kritiek" or OPDRACHT in ["1c", "1e"]:
        boolean = True
    else:
        boolean = False
        
    for conn in list_with_connections:
        if station[0] in [conn.station1, conn.station2]:
            if boolean:
                conn.setCritic(boolean)

uitkomsten = []
aantallen = []

statespace = statespace()
statespace_lijst = statespace[0]
statespace_afstanden = statespace[1]

for loop in range(10000):
    print(loop)
    for c in list_with_connections:
        c.setUsed(False)
        
    list_with_trajects = []
    
    for i in range(12):
        index = random.randint(0, len(statespace_lijst) - 1)
        new = TRAJECT()
        new.stations = statespace_lijst[index][:]
        new.total_time = statespace_afstanden[index]
        list_with_trajects.append(new)
    
    for t in list_with_trajects:
        for s in range(len(t.stations)-1):
            for c in list_with_connections:
                if sorted([t.stations[s], t.stations[s+1]]) == sorted([c.station1, c.station2]):
                    c.setUsed(True)
                  
    doel = doelfunctie(list_with_connections, list_with_trajects)
    if doel in uitkomsten:
        index_doel = uitkomsten.index(doel)
        aantallen[index_doel] = aantallen[index_doel] + 1
    else:
        uitkomsten.append(doel)
        aantallen.append(1)
    
for i in range(len(uitkomsten)-1):
    exportfile.write(str(uitkomsten[i]) + "-" + str(aantallen[i]))
    exportfile.write("\n")

exportfile.close() 
