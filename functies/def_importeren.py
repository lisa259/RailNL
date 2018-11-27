import csv
import os

def importeren(OPDRACHT):
    if OPDRACHT in ["1a", "1b", "1c"]:
        naam_connecties = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'csv', 'ConnectiesHolland.csv')
        name_stations = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'csv', 'StationsHolland.csv')
        
    bestand_connecties = open(naam_connecties, encoding='utf-8-sig')
    all_connections = csv.reader(bestand_connecties)
    
    file_stations = open(name_stations, encoding='utf-8-sig')
    all_stations = csv.reader(file_stations)
    
    return [all_connections, all_stations, bestand_connecties, file_stations]