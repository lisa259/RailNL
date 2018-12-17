import math
import random  

class TRAJECT:
    def __init__(self):
        self.stations = []
        self.total_time = 0
    def addStation(self, station, index):
        if index == "begin":
            self.stations = [station] + self.stations
        elif index == "end":
            self.stations.append(station)
    def addTotal_time(self, time):
        self.total_time += time
        
    " TRAJECT UITBREIDEN "
    def new_connection(self, list_with_connections, MAX_AANTAL_MINUTEN, TRAJECT_UITBREIDEN):
        shortest = None
        
        # Random/kritiek/ongebruikte connectie dat aansluit op traject toevoegen
        if TRAJECT_UITBREIDEN == "random":
            lijstje = []
            # zoek ongebruikte, kritiek sporen, die aansluiten op station1 of station2
            for conn in list_with_connections:
                if conn.critic == True and conn.used == False and (conn.station1 == self.stations[0] or conn.station1 == self.stations[-1] or conn.station2 == self.stations[0] or conn.station2 == self.stations[-1]):
                    lijstje.append(conn)
            
            while lijstje:
                # Kies random 1 van de geschikte sporen
                gebruiken = random.choice(lijstje)
                if self.total_time + gebruiken.duration <= MAX_AANTAL_MINUTEN:
                    if self.stations[0] == gebruiken.station1:
                        self.addStation(gebruiken.station2, "begin")
                    elif self.stations[0] == gebruiken.station2:
                        self.addStation(gebruiken.station1, "begin")
                    elif self.stations[-1] == gebruiken.station1:
                        self.addStation(gebruiken.station2, "end")
                    elif self.stations[-1] == gebruiken.station2:
                        self.addStation(gebruiken.station1, "end")
                    self.addTotal_time(gebruiken.duration)
                    gebruiken.setUsed(True)
                    return True
                else:
                    lijstje.remove(gebruiken)
                
            # geen spoor gevonden om toe te kunnen voegen
            return False
        
        # kortste/kritiek/ongebruikte connectie dat aansluit op traject toevoegen
        elif TRAJECT_UITBREIDEN == "min":
            minimum = math.inf
            # zoekt kortste, ongebruikte, kritiek spoore, dat aansluit op station1 of station2
            for conn in list_with_connections:
                if conn.critic == True and conn.used == False and conn.duration < minimum and (conn.station1 == self.stations[0] or conn.station1 == self.stations[-1] or conn.station2 == self.stations[0] or conn.station2 == self.stations[-1]):
                    minimum = conn.duration
                    shortest = conn
        
        # langste/kritiek/ongebruikte connectie dat aansluit op traject toevoegen        
        elif TRAJECT_UITBREIDEN == "max":
            minimum = 0
            # zoekt langste, ongebruikte, kritiek spoore, dat aansluit op station1 of station2
            for conn in list_with_connections:
                if conn.critic == True and conn.used == False and conn.duration > minimum and (conn.station1 == self.stations[0] or conn.station1 == self.stations[-1] or conn.station2 == self.stations[0] or conn.station2 == self.stations[-1]):
                    minimum = conn.duration
                    shortest = conn
                    
        # spoor gevonden en valt nog binnen de tijd: toevoegen aan traject
        if shortest != None and self.total_time + minimum <= MAX_AANTAL_MINUTEN:
            if self.stations[0] == shortest.station1:
                self.addStation(shortest.station2, "begin")
            elif self.stations[0] == shortest.station2:
                self.addStation(shortest.station1, "begin")
            elif self.stations[-1] == shortest.station1:
                self.addStation(shortest.station2, "end")
            elif self.stations[-1] == shortest.station2:
                self.addStation(shortest.station1, "end")
            self.addTotal_time(minimum)
            shortest.setUsed(True)
            return True
        # geen spoor gevonden om toe te kunnen voegen
        return False
        
        