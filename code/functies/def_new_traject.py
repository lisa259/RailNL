
from classes.class_TRAJECT import TRAJECT 
import math   
import random  

"NIEUW TRAJECT"
def new_traject(list_with_connections, TRAJECT_OPSTELLEN):
    shortest = None
    
    # Een random ongebruikt, kritiek spoor gebruiken
    if TRAJECT_OPSTELLEN == "random":
        # Lijst vullen met alle mogelijke sporen
        lijstje = []
        for conn in list_with_connections:
            if conn.critic == True and conn.used == False:
                lijstje.append(conn)
        if lijstje:
            # kies random 1 van de sporen
            gebruik = random.choice(lijstje)
            
            # opstellen traject
            new = TRAJECT()
            new.addStation(gebruik.station1, "end")
            new.addStation(gebruik.station2, "end")
            new.addTotal_time(gebruik.duration)
            gebruik.setUsed(True)
            return new
        return False
    
    # Het korste ongebruikte, kritieke spoor gebruiken
    elif TRAJECT_OPSTELLEN == "min":   
        minimum = math.inf
        # zoeken naar korste ongebruikte kritieke spoor
        for conn in list_with_connections:
            if conn.critic == True and conn.used == False and conn.duration < minimum:
                minimum = conn.duration
                shortest = conn
                
    # Het langste ongebruikte, kritieke spoor gebruiken
    elif TRAJECT_OPSTELLEN == "max": 
        minimum = 0
        # zoeken naar langste ongebruikte kritieke spoor
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
    
    
    