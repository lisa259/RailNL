import math
from copy import deepcopy
from functies.def_dijkstra import Dijkstra, deconstruct_path
from functies.def_doelfunctie import doelfunctie

" ONGEBRUIKTE KRITIEKE SPOREN TOEVOEGEN AAN BESTAANDE TRAJECTEN "
def linken(stations, time, list_with_trajects, list_with_stations, MAX_AANTAL_MINUTEN, doelwaarde, list_with_connections, connectie_index):
    # parameter stations is een list met de 2 stations van de ongebruikte connectie
    minimum = math.inf
    
    for add_station in stations:
        # dijkstra returnt een dictionary met stations + korste afstand naar dit station en een dictionary met stations + voorgegaande station
        dijkstra = Dijkstra(add_station, list_with_stations)
        verbindingen = dijkstra[0]
        parents = dijkstra[1]
       
        # Opslaan van de korste route om het station te linken 
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
        path = deconstruct_path(safe_parents, end)
        if end == in_traject.stations[0]:
            plek = "begin"
        elif end == in_traject.stations[-1]:
            plek = "end"
        if path != None:  
            # kopieën
            index_traject = list_with_trajects.index(in_traject)
            copy_trajecten = deepcopy(list_with_trajects)
            copy_connections = deepcopy(list_with_connections)
            copy_trajecten[index_traject].addTotal_time(minimum + time)
            
            # path toevoegen aan traject
            for index in range(1, len(path)):
                copy_trajecten[index_traject].addStation(path[index], plek)
            if copy_trajecten[index_traject].stations[-2] != toevoegen:
                copy_trajecten[index_traject].addStation(toevoegen, plek)
            copy_connections[connectie_index].setUsed(True)
            
            # Betere doelwaarde?
            if doelwaarde <= doelfunctie(copy_connections, copy_trajecten):
            
                in_traject.addTotal_time(minimum + time)
                # path toevoegen aan traject
                for index in range(1, len(path)):
                    in_traject.addStation(path[index], plek)
                # andere station uit connectie ook toevoegen
                if in_traject.stations[-2]  != toevoegen:
                    in_traject.addStation(toevoegen, plek)
                return True
    return False