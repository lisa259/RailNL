
from classes.class_TRAJECT import TRAJECT 
import math   
import random  

"NIEUW TRAJECT"
def new_traject(list_with_connections, TRAJECT_OPSTELLEN):
    shortest = None
    if TRAJECT_OPSTELLEN == "random":
        lijstje = []
        for conn in list_with_connections:
            if conn.critic == True and conn.used == False:
                lijstje.append(conn)
        if lijstje:
            gebruik = random.choice(lijstje)
            new = TRAJECT()
            new.addStation(gebruik.station1, "end")
            new.addStation(gebruik.station2, "end")
            new.addTotal_time(gebruik.duration)
            gebruik.setUsed(True)
            return new
        return False
    elif TRAJECT_OPSTELLEN == "min":   
        minimum = math.inf
        # zoeken naar korste ongebruikte kritieke spoor
        for conn in list_with_connections:
            if conn.critic == True and conn.used == False and conn.duration < minimum:
                minimum = conn.duration
                shortest = conn
    elif TRAJECT_OPSTELLEN == "max": 
        minimum = 0
        # zoeken naar korste ongebruikte kritieke spoor
        for conn in list_with_connections:
            if conn.critic == True and conn.used == False and conn.duration > minimum:
                minimum = conn.duration
                shortest = conn
    # spoor gevonden: nieuw traject van maken
    if shortest != None:
        new = TRAJECT()
        new.addStation(shortest.station1, "end")
        new.addStation(shortest.station2, "end")
        new.addTotal_time(minimum)
        shortest.setUsed(True)
        return new
    # geen spoor gevonden
    return False
    
    
    