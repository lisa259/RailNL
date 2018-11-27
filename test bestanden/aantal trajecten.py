" AANTAL TRAJECTEN BINNEN 120 MINUTEN "

import os
import csv
import copy

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

write = open(os.path.join(os.path.dirname(__file__), 'export.csv'), mode='w')
writer = csv.writer(write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

trajecten = []
alles = {}
length = 2
uitgebreid = True
while uitgebreid == True:
    if length == 2:
        for conn in list_with_connections:
            verbinding = TRAJECT()
            verbinding.addStation(conn.station1, "end")
            verbinding.addStation(conn.station2, "end")
            verbinding.addTotal_time(conn.duration)
            writer.writerow(verbinding.stations)
            trajecten.append(verbinding)
    else:
        uitgebreid = False
        for traject in alles[length-1]:
            # geeft ieder traject van 2 stations
            # nu alles uitbreiden
            writer.writerow(str(length))
            for conn in list_with_connections:
                traj = copy.deepcopy(traject)
                if traj.stations[0] == conn.station1 and traj.total_time + conn.duration <= 120:
                    traj.addStation(conn.station2, "begin")
                    traj.addTotal_time(conn.duration)
                    trajecten.append(traj)
                    uitgebreid = True
                    writer.writerow(traj.stations)
                elif traj.stations[-1] == conn.station1 and traj.total_time + conn.duration <= 120:
                    traj.addStation(conn.station2, "end")
                    traj.addTotal_time(conn.duration)
                    trajecten.append(traj)
                    uitgebreid = True
                    writer.writerow(traj.stations)
                elif traj.stations[0] == conn.station2 and traj.total_time + conn.duration <= 120:
                    traj.addStation(conn.station1, "begin")
                    traj.addTotal_time(conn.duration)
                    trajecten.append(traj)
                    uitgebreid = True
                    writer.writerow(traj.stations)
                elif traj.stations[-1] == conn.station2 and traj.total_time + conn.duration <= 120:
                    traj.addStation(conn.station1, "end")
                    traj.addTotal_time(conn.duration)
                    trajecten.append(traj)
                    uitgebreid = True
                    writer.writerow(traj.stations)
    if trajecten != []:
        alles[length] = trajecten
    trajecten = [] 
    print("length {} done".format(length))
    writer.writerow("")
    length += 1
  
lijstje = {}
aantal = 0
for key_tr in alles:
    print("--------- {} --------------".format(key_tr))
    for value_tr in alles[key_tr]:
        aantal += 1
        print(value_tr.stations)
#        dubbel = False
#        if key_tr in lijstje:
#            for item in lijstje[key_tr]:
#                if sorted(value_tr.stations) == sorted(item.stations):
#                    dubbel = True
#            if dubbel == False:
#                lijstje[key_tr].append(value_tr)
#        else:
#            lijstje[key_tr] = [value_tr]
#        
#aantall = 0      
#for x in lijstje:
#    print("--------{}--------".format(x))
#    if x < 4:
#        for y in lijstje[x]:
#            aantall += 0
#            print(y.stations)
#            print(y.total_time)
#print(lijstje)          
            
#print(alles)
print(aantal)
























