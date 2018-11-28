import random
from copy import deepcopy
from functies.def_doelfunctie import doelfunctie

def hill_climbing(list_with_trajects, list_with_stations, list_with_connections):
    #random 1 traject uit list_with_trajects kiezen    v 
    #random 2 plaatsen uit traject kiezen              v
    #check if connectie bestaat als omgedraaid         v
    #maak copy list_with_trajects                      v
    #draai plaatsen om                                 v
    #hogere doelwaarde? kopie als origineel nemen, anders door met origineel
    traject = random.choice(list_with_trajects)
#    print(traject.stations)
    if len(traject.stations) > 2:  
        station1 = random.choice(traject.stations)
        station2 = random.choice(traject.stations)
#        print(station1)
#        print(station2)
        index1 = traject.stations.index(station1)
        index2 = traject.stations.index(station2)
        
        check = 0
        nodig = 0
        
        # onzin om met jezelf te ruilen
        if station1 != station2:
            # station2 niet aan buitenkanten traject, om te weten dat er 2 buren zijn
            if len(traject.stations)-1 > index2 > 0:
                nodig += 2
                
                # connecties station1 ophalen
                for station in list_with_stations:
                    if station.name == station1:
                        for connection in station.connections:
                            # buren van station2 in connecties?
                            if traject.stations[index2 - 1] in [connection.station1, connection.station2] and traject.stations[index2 - 1] != station.name:
                                check += 1
                            if traject.stations[index2 + 1] in [connection.station1, connection.station2] and traject.stations[index2 + 1] != station.name:
                                check += 1
                                
                                
            # station1 niet aan buitenkanten traject, om te weten dat er 2 buren zijn
            if len(traject.stations)-1 > index1 > 0:
                nodig += 2
                
                # connecties station2 ophalen
                for station in list_with_stations:
                    if station.name == station2:
                        for connection in station.connections:
                            # buren van station1 in connecties?
                            if traject.stations[index1 - 1] in [connection.station1, connection.station2] and traject.stations[index1 - 1] != station.name:
                                check += 1
                            if traject.stations[index1 + 1] in [connection.station1, connection.station2] and traject.stations[index1 + 1] != station.name:
                                check += 1
                                
            
            # station2 aan begin, station1 moet connectie hebben met [1]
            if index2 == 0:
                nodig += 1
                # connecties station1 ophalen
                for station in list_with_stations:
                    if station.name == station1:
                        for connection in station.connections:
                            # buur van station2 in connecties?
                            if traject.stations[1] in [connection.station1, connection.station2] and traject.stations[1] != station.name:
                                check += 1
                                
            
            # station1 aan begin, station2 moet connectie hebben met [1]
            if index1 == 0:
                nodig += 1
                # connecties station2 ophalen
                for station in list_with_stations:
                    if station.name == station2:
                        for connection in station.connections:
                            # buur van station2 in connecties?
                            if traject.stations[1] in [connection.station1, connection.station2] and traject.stations[1] != station.name:
                                check += 1
                                
                                
            # station2 aan eind, station1 moet connectie hebben met [-2]
            if index2 == len(traject.stations)-1:
                nodig += 1
                # connecties station1 ophalen
                for station in list_with_stations:
                    if station.name == station1:
                        for connection in station.connections:
                            # buur van station2 in connecties?
                            if traject.stations[-2] in [connection.station1, connection.station2] and traject.stations[-2] != station.name:
                                check += 1
                                
            # station1 aan eind, station2 moet connectie hebben met [-2]
            if index1 == len(traject.stations)-1:
                nodig += 1
                # connecties station1 ophalen
                for station in list_with_stations:
                    if station.name == station2:
                        for connection in station.connections:
                            # buur van station1 in connecties?
                            if traject.stations[-2] in [connection.station1, connection.station2] and traject.stations[-2] != station.name:
                                check += 1
          
            if nodig == check: 
                copy_traject = deepcopy(traject) 
                copy_traject.stations[index1], copy_traject.stations[index2] = copy_traject.stations[index2], copy_traject.stations[index1]
#                print(copy_traject.stations)
                copy_list_with_trajects = deepcopy(list_with_trajects)
                index_traject = list_with_trajects.index(traject)
                copy_list_with_trajects[index_traject] = deepcopy(copy_traject)
                if doelfunctie(list_with_connections, list_with_trajects) < doelfunctie(list_with_connections, copy_list_with_trajects):
                    print("joe")
                    return copy_list_with_trajects
                
    return False
        