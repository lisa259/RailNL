# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:26:50 2018

@author: My Lenovo
"""
import os
import xlrd

""" IMPORT CONNECTIES BESTAND """
naam_connecties = os.path.join(os.path.dirname(__file__), 'ConnectiesHolland.xlsx')
bestand_connecties = xlrd.open_workbook(naam_connecties)
sheet1_connecties = bestand_connecties.sheet_by_index(0)
nrows1_connecties = sheet1_connecties.nrows

""" IMPORT STATIONS FILE """
name_stations = os.path.join(os.path.dirname(__file__), 'StationsHolland.xlsx')
file_stations = xlrd.open_workbook(name_stations)
sheet1_stations = file_stations.sheet_by_index(0)
nrows1_stations = sheet1_stations.nrows

""" PUT ALL CONNECTIONS LIKE LIST IN LIST """
list_with_connections = []
for i in range(0, nrows1_connecties):
    # van ['plaats1, plaats2, afstand'] naar 'plaats1, plaats2, afstand'
    string = sheet1_connecties.row_values(i)[0] 
    
    # van 'plaats1, plaats2, afstand' naar ["plaats1", "plaats2", "afstand"] 
    connection = string.split(',')
    
    # van ["plaats1", "plaats2", "afstand"] naar ["plaats1", "plaats2", afstand] 
    connection[2] = int(connection[2])
    
    list_with_connections.append(connection)
    
""" PUT ALL STATIONS + BOOLEAN OF CRITIC IN LIST"""
list_with_stations = []
for i in range(0, nrows1_stations):
    # van ['station, x, y, (Kritiek)'] naar 'station, x, y, (Kritiek)'
    string = sheet1_stations.row_values(i)[0] 
    
    # van 'station, x, y, (Kritiek)' naar ["station", boolean kritiek] 
    station = []
    station.append(string.split(',')[0])
    if string.split(',')[-1] == "Kritiek":
        station.append(True)
    else:
        station.append(False)

    list_with_stations.append(station)

print(list_with_connections)
#print(list_with_stations)


""" PUT ALL INFORMATION IN CLASSES """

class CONNECTION:
    def __init__(self, station1, station2, duration):
        self.station1 = station1
        self.station2 = station2
        self.duration = duration
        self.critic = False
        self.used = False

#empty list for classes connections
classes_connections = []
for i in range(0, len(list_with_connections)):
    connection = CONNECTION(list_with_connections[i][0], list_with_connections[i][1], list_with_connections[i][2],)
    classes_connections.append(connection)
    
#print(classes_connections[0].critic)

class STATION:
    def __init__(self, name, critic, connections):
        self.name = name
        self.critic = critic
        self.used = False
        self.connections = connections
        
#empty list for classes stations
classes_stations = []
for i in range(0, len(list_with_stations)):
    #empty list for connections conected to a station
    connections_station = []
    #iterate over all connections
    for j in range(0, len(classes_connections)):
        name = list_with_stations[i][0]
        #if name of station in connection on place station1 or station 2
        if name in classes_connections[j].station1 or name in classes_connections[j].station2:
            #append this connection to connection list of the station
            connections_station.append(classes_connections[j])
    #make class
    station = STATION(list_with_stations[i][0], list_with_stations[i][1], connections_station)
    classes_stations.append(station)
    
#print(classes_stations[0].connections[1].station2)

#critic of connections change
for i in range(0, len(classes_connections)):
    # save name station1
    station1 = classes_connections[i].station1
    station2 = classes_connections[i].station2
    #iterate over all stations
    for j in range (0, len(classes_stations)):
        # if station1 is the station and station is critic
        if classes_stations[j].name == station1 and classes_stations[j].critic == True:
            # connection is critic
            classes_connections[i].critic = True
        elif classes_stations[j].name == station2 and classes_stations[j].critic == True:
            classes_connections[i].critic = True

#print(classes_connections[24].station1)
#print(classes_connections[24].station2)
#print(classes_connections[24].critic)
        
class TRAJECT:
    def __init__(self, stations, total_time):
        self.stations = stations
        self.total_time = total_time

""" ONDERSTAANDE MATRIXSHIT WAARSCHIJNLIJK NIET MEER NODIG """    
#""" MAAK LEGE MATRIX """
#matrix = []
#for i in range(0, len(list_met_stations) + 1):
#    row = []
#    for j in range(0, len(list_met_stations) + 1):
#        row.append("")
#    matrix.append(row)
#
#""" VUL RIJ 0 EN KOLOM 0 VAN MATRIX MET STATIONS """
#for i in range(1, len(list_met_stations) + 1):
#    matrix[0][i] = list_met_stations[i-1]
#    matrix[i][0] = list_met_stations[i-1]
#
#""" VUL REST VAN MATRIX MET CONNECTIEAFSTAND """
#for i in range(0, len(list_met_connecties)):
#    index1 = list_met_stations.index(list_met_connecties[i][0])
#    index2 = list_met_stations.index(list_met_connecties[i][1])
#    
#    matrix[index1 + 1][index2 + 1] = list_met_connecties[i][2]
#    matrix[index2 + 1][index1 + 1] = list_met_connecties[i][2]
#
#""" VIND LAAGSTE AFSTAND IN MATRIX """
#laagste = 100000
#for i in range(1, len(list_met_stations) + 1):
#    for j in range(1, len(list_met_stations) + 1):
#        if matrix[i][j] != "" and matrix[i][j] < laagste:
#            laagste = matrix[i][j]
#            
#
## CLASS CONNECTIE : 2 stations, afstand, kritiek?, gebruikt?
##? CLASS STATION: connecties, kritiek?, gebruikt?
## CLASS TRAJECT: stations, totale tijd
