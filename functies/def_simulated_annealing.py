import random
from copy import deepcopy
from functies.def_doelfunctie import doelfunctie

def simulated_annealing(list_with_trajects, list_with_stations, list_with_connections):
    
    
    # lengte tabu, kan veranderen naar wat je wil !!!!!!!!!!!!!!!!!!!!!!!1
    lengte = 3
    # tabu list
    tabu = []
    # random traject kiezen
    traject = random.choice(list_with_trajects)
    # boolean for in tabu
    controle = False
    #
    vergelijking1 = 0
    vergelijking2 = 0
    
    if len(traject.stations) > 2:  
        station1 = random.choice(traject.stations)
        station2 = random.choice(traject.stations)
#        print(station1)
#        print(station2)
        index1 = traject.stations.index(station1)
        index2 = traject.stations.index(station2)
        
        # aantal buren die station 1 en 2 samen hebben
        check = 0
        # aantal nieuwe connecties die gemaakt kunnen worden met de nieuwe buren als er geruil wordt
        nodig = 0
        # variabele voor of een station aan de buitenkant zit of niet
        wissel1 = "null"
        wissel2 = "null"
        
        oud1 = 0
        nieuw1 = 0
        oud2 = 0
        nieuw2 = 0
        
        
        
        # onzin om met jezelf te ruilen
        if station1 != station2:
            # station2 niet aan buitenkanten traject, om te weten dat er 2 buren zijn
            if len(traject.stations)-1 > index2 > 0:
                nodig += 2
                wissel2 = "binnen"
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
                wissel1 = "binnen"
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
                wissel2 = "begin"
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
                wissel1 = "begin"
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
                wissel2 = "eind"
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
                wissel1 = "eind"
                # connecties station1 ophalen
                for station in list_with_stations:
                    if station.name == station2:
                        for connection in station.connections:
                            # buur van station1 in connecties?
                            if traject.stations[-2] in [connection.station1, connection.station2] and traject.stations[-2] != station.name:
                                check += 1
             
                   
            if nodig == check: 
                copy_traject = deepcopy(traject)
                
                # oude connecties opslaan station 1
                if wissel1 == "binnen":
                    if copy_traject.stations[index1 - 1] != station2:
                        oud1 = copy_traject.stations[index1 - 1]
                    else:
                        oud1 = copy_traject.stations[index1 + 1]
                elif wissel1 == "begin":
                    oud1 = copy_traject.stations[index1 + 1]
                elif wissel1 == "eind":
                    oud1 = copy_traject.stations[index1 - 1]
                tabu1 = [station1, oud1]
                if len(tabu) <= (lengte * 2):
                    tabu.append(tabu1)
                else:
                    tabu.remove((lengte * 2) - 1)
                    tabu = [tabu1] + tabu
                
                # oude connecties opslaan station 2
                if wissel2 == "binnen":
                    if copy_traject.stations[index2 - 1] != station1:
                        oud2 = copy_traject.stations[index2 - 1]
                    else:
                        oud2 = copy_traject.station[index2 + 1]
                elif wissel2 == "begin":
                    oud2 = copy_traject.stations[index2 + 1]
                elif wissel2 == "eind":
                    oud2 = copy_traject.stations[index2 - 1]
                tabu2 = [station2, oud2]
                if len(tabu) <= (lengte * 2):
                    tabu.append(tabu2)
                else:
                    tabu.remove((lengte * 2) - 1)
                    tabu = [tabu2] + tabu
                
                # verwisselen van stations
                copy_traject.stations[index1], copy_traject.stations[index2] = copy_traject.stations[index2], copy_traject.stations[index1]
               
                # nieuwe connecties opslaan station 1
                if wissel2 == "binnen":
                    if copy_traject.stations[index2 - 1] != station2:
                        nieuw1 = copy_traject.stations[index2 - 1]
                    else:
                        nieuw1 = copy_traject.stations[index2 + 1]
                elif wissel2 == "eind":
                    nieuw1 = copy_traject.stations[index2 - 1]
                elif wissel2 == "begin":
                    nieuw1 = copy_traject.stations[index2 + 1]
                vergelijking1 = [station1, nieuw1]
                    
                # nieuwe connecties opslaan station 2
                if wissel1 == "binnen":
                    if copy_traject.stations[index1 - 1] != station1:
                        nieuw2 = copy_traject.stations[index1 - 1]
                    else:
                        nieuw2 = copy_traject.stations[index1 + 1]
                elif wissel1 == "eind":
                    nieuw2 = copy_traject.stations[index1 - 1]
                elif wissel1 == "begin":
                    nieuw2 = copy_traject.stations[index1 + 1]
                vergelijking2 = [station2, nieuw2]

                if len(tabu) >= 1:
                    for part in tabu:
                        if vergelijking1[0] in part and vergelijking1[1] in part and vergelijking2[0] in part and vergelijking2[1] in part:
                            controle = True
                        

#                 print(copy_traject.stations)
                copy_list_with_trajects = deepcopy(list_with_trajects)
                index_traject = list_with_trajects.index(traject)
                copy_list_with_trajects[index_traject] = deepcopy(copy_traject)
                if doelfunctie(list_with_connections, list_with_trajects) < doelfunctie(list_with_connections, copy_list_with_trajects) and controle == False:
                    print("joe")
                    return copy_list_with_trajects
                else:
                    print("verslechtering")
                    # tabu list vullen met wat we weg nemen
                    # in if vragen of toevoegende connecties in tabu list zitten
                    # zo niet, dan accepteren
                    # zo wel, dan niet accepteren, want dan doe je een stap terug
                    # nieuwe meegeven
                    
                
    return False
            
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                