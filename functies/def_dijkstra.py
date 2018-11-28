import math

" ALGORITME VAN DIJKSTRA "          
def Dijkstra(current, list_with_stations):
    # maak dictionary van onbezochte stations met afstand vanaf beginpunt. zet afstand nu op infinity
    unvisited = {station.name: math.inf for station in list_with_stations}
    visited = {}
    currentDistance = 0
    # set de afstand van current (begin) station op 0
    unvisited[current] = currentDistance
    #dictionary die opslaat wat de voorganger van een station is
    parents = {}
        
    #bepaal korste afstand van beginstation naar alle andere stations
    while True:
        for station in list_with_stations:
            if current == station.name:
                # alle connecties van huidig station afgaan
                for connectie in station.connections:
                    # sla aansluitend station op als neighbour
                    if current == connectie.station1:
                        neighbour = connectie.station2
                    elif current == connectie.station2:
                        neighbour = connectie.station1
                    if neighbour not in unvisited: continue
                
                    
                    newDistance = currentDistance + connectie.duration
                    
                    if unvisited[neighbour] > newDistance:
                        unvisited[neighbour] = newDistance
                        # add neighbour en current als link toe aan dictionary
                        parents[neighbour] = current
                        
        # sla current station op als bezocht en verwijder uit onbezocht      
        visited[current] = currentDistance
        del unvisited[current]
        
        # geen onbezochte stations meer over
        if not unvisited: break
        
        # lijst met (neighbour, afstand)
        candidates = [node for node in unvisited.items() if node[1]]
        # neemt station met korste afstand als nieuwe current
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return [visited, parents]

" PATH VAN DIJKSTRA OPSTELLEN: VAN GEVRAAGD NAAR BEGIN STATION "
def deconstruct_path(parents, end):
    if end not in parents:
        # geen path mogelijk
        return None
    
    gezocht = end
    path = []
    while gezocht:
        path.append(gezocht)
        # set gezocht op voorgaande station van huidig gezocht
        gezocht = parents.get(gezocht)
    return path