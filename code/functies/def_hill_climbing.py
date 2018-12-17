import random
from copy import deepcopy
from functies.def_doelfunctie import doelfunctie

def hill_climbing(list_with_trajects, list_with_stations, list_with_connections):

    # Random traject
    traject = random.choice(list_with_trajects)

    if len(traject.stations) > 2: 
        # 2 random stations uit geselecteerde traject
        station1 = random.choice(traject.stations)
        station2 = random.choice(traject.stations)

        index1 = traject.stations.index(station1)
        index2 = traject.stations.index(station2)
        
        check = 0 # Aantal kloppende connecties (Bij verwisselen)
        nodig = 0 # Aantal connecties dat gemaakt moet kunnen worden
        
        conn_nieuw = []
        conn_oud = []
        
        # onzin om met jezelf te ruilen
        if station1 != station2:
            # station2 niet aan buitenkanten traject, station2 heeft 2 buren
            if len(traject.stations)-1 > index2 > 0:
                nodig += 2
                
                conn_oud.append(sorted([station2, traject.stations[index2-1]]))
                conn_oud.append(sorted([station2, traject.stations[index2+1]]))
                conn_nieuw.append(sorted([station1, traject.stations[index2-1]]))
                conn_nieuw.append(sorted([station1, traject.stations[index2+1]]))
                
                # connecties station1 ophalen
                for station in list_with_stations:
                    if station.name == station1:
                        for connection in station.connections:
                            # buren van station2 in connecties?
                            if traject.stations[index2 - 1] in [connection.station1, connection.station2] and traject.stations[index2 - 1] != station.name:
                                check += 1
                            if traject.stations[index2 + 1] in [connection.station1, connection.station2] and traject.stations[index2 + 1] != station.name:
                                check += 1
                                
                                
            # station1 niet aan buitenkanten traject, station1 heeft 2 buren
            if len(traject.stations)-1 > index1 > 0:
                nodig += 2
                
                conn_oud.append(sorted([station1, traject.stations[index1-1]]))
                conn_oud.append(sorted([station1, traject.stations[index1+1]]))
                conn_nieuw.append(sorted([station2, traject.stations[index1-1]]))
                conn_nieuw.append(sorted([station2, traject.stations[index1+1]]))
                
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
                
                conn_oud.append(sorted([station2, traject.stations[index2+1]]))
                conn_nieuw.append(sorted([station1, traject.stations[index2+1]]))
                
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
                
                conn_oud.append(sorted([station1, traject.stations[index1+1]]))
                conn_nieuw.append(sorted([station2, traject.stations[index1+1]]))
                
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
                
                conn_oud.append(sorted([station2, traject.stations[index2-1]]))
                conn_nieuw.append(sorted([station1, traject.stations[index2-1]]))
                
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
                
                conn_oud.append(sorted([station1, traject.stations[index1-1]]))
                conn_nieuw.append(sorted([station2, traject.stations[index1-1]]))
                
                # connecties station1 ophalen
                for station in list_with_stations:
                    if station.name == station2:
                        for connection in station.connections:
                            # buur van station1 in connecties?
                            if traject.stations[-2] in [connection.station1, connection.station2] and traject.stations[-2] != station.name:
                                check += 1
          
            # Stations kunnen van plek gewisseld worden
            if nodig == check: 
                # Levert het een betere kwaliteit op?
                copy_traject = deepcopy(traject) 
                copy_traject.stations[index1], copy_traject.stations[index2] = copy_traject.stations[index2], copy_traject.stations[index1]
                copy_list_with_trajects = deepcopy(list_with_trajects)
                index_traject = list_with_trajects.index(traject)
                copy_list_with_trajects[index_traject] = deepcopy(copy_traject)
                
                copy_connections = deepcopy(list_with_connections)
                for c in copy_connections:
                    # if oude connectie: 
                    if sorted([c.station1, c.station2]) in conn_oud: 
                        c.used = False
                    # if nieuwe connectie:
                    if sorted([c.station1, c.station2]) in conn_nieuw:
                        c.used = True
                        
                if doelfunctie(list_with_connections, list_with_trajects) < doelfunctie(copy_connections, copy_list_with_trajects):
                    return [copy_list_with_trajects, copy_connections]
                
    return False
        