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

""" IMPORT STATIONS BESTAND """
naam_stations = os.path.join(os.path.dirname(__file__), 'StationsHolland.xlsx')
bestand_stations = xlrd.open_workbook(naam_stations)
sheet1_stations = bestand_stations.sheet_by_index(0)
nrows1_stations = sheet1_stations.nrows

""" PLAATS ALLE CONNECTIES ALS LIST IN LIST """
list_met_connecties = []
for i in range(0, nrows1_connecties):
    # van ['plaats1, plaats2, afstand'] naar 'plaats1, plaats2, afstand'
    string = sheet1_connecties.row_values(i)[0] 
    
    # van 'plaats1, plaats2, afstand' naar ["plaats1", "plaats2", "afstand"] 
    connectie = string.split(',')
    
    # van ["plaats1", "plaats2", "afstand"] naar ["plaats1", "plaats2", afstand] 
    connectie[2] = int(connectie[2])
    
    list_met_connecties.append(connectie)
    
""" PLAATS ALLE STATIONS + BOOLEAN OF KRITIEK IN LIST"""
list_met_stations = []
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

    list_met_stations.append(station)


#print(list_met_stations)
# 
#    ####### CLASSES INDELEN
#

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
