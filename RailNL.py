# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:26:50 2018

@author: My Lenovo
"""

import xlrd
""" IMPORT CONNECTIES BESTAND """
lisa_connecties = r"C:\Users\My Lenovo\Downloads/ConnectiesHolland.xlsx"
bestand_connecties = xlrd.open_workbook(lisa_connecties)
sheet1_connecties = bestand_connecties.sheet_by_index(0)
nrows1_connecties = sheet1_connecties.nrows

""" IMPORT KRITIEK BESTAND """
lisa_kritiek = r"C:\Users\My Lenovo\Downloads/StationsHolland.xlsx"
bestand_kritiek = xlrd.open_workbook(lisa_kritiek)
sheet1_kritiek = bestand_kritiek.sheet_by_index(0)
nrows1_kritiek = sheet1_kritiek.nrows

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
    
    
#print(list_met_connecties)
#print(list_met_connecties[0][0]) # = plaats1

list_met_stations = []
for i in range(0, nrows1_kritiek):
    # van ['plaats1, plaats2, afstand'] naar 'plaats1, plaats2, afstand'
    string = sheet1_kritiek.row_values(i)[0] 
    
    # van 'plaats1, plaats2, afstand' naar ["plaats1", "plaats2", "afstand"] 
    station = []
    station.append(string.split(',')[0])
    if string.split(',')[-1] == "Kritiek":
        station.append(True)
    else:
        station.append(False)

    
    list_met_stations.append(station)


#""" PLAATS ALLE STATIONS IN LIST """
#list_met_stations = []
#for i in list_met_connecties:
#    if i[0] not in list_met_stations:
#        list_met_stations.append(i[0])
#    if i[1] not in list_met_stations:
#        list_met_stations.append(i[1])
#        
print(list_met_stations)

#""" PLAATS ALLE KRITIEKE STATIONS IN LIJST """
#list_met_kritieke_stations = []
#for i in range(0, nrows1_kritiek):
#    if sheet1_kritiek.row_values(i)[0].split(',')[-1] == "Kritiek":
#        list_met_kritieke_stations.append(sheet1_kritiek.row_values(i)[0].split(',')[0])
#        
##print(list_met_kritieke_stations)
# 
#    ####### CLASSES INDELEN
#    
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
