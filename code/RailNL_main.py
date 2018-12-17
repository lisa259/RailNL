from classes.class_STATION import STATION
from classes.class_CONNECTION import CONNECTION

from functies.def_new_traject import new_traject
from functies.def_importeren import importeren
from functies.def_linken import linken
from functies.def_doelfunctie import doelfunctie
from functies.def_plotten import plotten
from functies.def_hill_climbing import hill_climbing
from functies.def_simulated_annealing import simulated_annealing

from copy import deepcopy



" BEPALEN VARIABELEN "

# Vraag de gebruiker welke opdracht uitgevoerd moet worden
while True:
    OPDRACHT = input("Welke opdracht wilt u uitvoeren? Kies uit 1a, 1b, 1c, 1d, 1e, 1h : ")
    if OPDRACHT in ["1a", "1b", "1c", "1d", "1e", "1h"]:
        print("Even geduld aub..")
        print("")
        break

# Manier waarop het traject opgesteld/uitgebreid wordt
TRAJECT_OPSTELLEN = "random"    # "min", "max", "random"
TRAJECT_UITBREIDEN = "random"   # "min", "max", "random"

aantalLoops = 1
if TRAJECT_OPSTELLEN == "random" or TRAJECT_UITBREIDEN == "random":
    aantalLoops = 5000
    
# Vaststellen grenzen aantal trajecten en minuten per traject
if OPDRACHT == "1a":
    variabelen = [4, 4, 120, 120]
elif OPDRACHT == "1b" or OPDRACHT == "1c":
    variabelen = [4, 4, 120, 120]
elif OPDRACHT == "1d":
    variabelen = [9, 9, 180, 180]
elif OPDRACHT == "1e":
    variabelen = [12, 12, 180, 180]
elif OPDRACHT == "1h":
    variabelen = [8, 8, 180, 180]
    
MIN_TREINEN = variabelen[0]
MAX_TREINEN = variabelen[1]   
MIN_MINUTEN = variabelen[2]
MAX_MINUTEN = variabelen[3]

# importeren gegevens van cvs bestanden
bestanden = importeren(OPDRACHT)
all_connections = bestanden[0]
all_stations = bestanden[1]




" GEGEVENS CVS VERWERKEN "
# Stop alle connecties als een CONNECTION-object in een lijst
list_with_connections = []
utrechtjes = []
for connection in all_connections:
    
    if OPDRACHT == "1h" and "Utrecht Centraal" in [connection[0], connection[1]]:
        utrechtjes.append([connection[0], connection[1]][[connection[0], connection[1]].index("Utrecht Centraal") -1])
        continue
    
    list_with_connections.append(CONNECTION(connection[0], connection[1], float(connection[2])))

    
# Stop alle stations als een STATIONS-object in een lijst
list_with_stations = []
for station in all_stations:
    if OPDRACHT == "1h" and station[0] == "Utrecht Centraal":
        continue
    boolean = False
    # bij 1c en 1e zijn alle stations/sporen kritiek
    if station[-1] == "Kritiek" or OPDRACHT in ["1c", "1e"]:
        boolean = True
        
    # Verzamel alle connecties die bij het station horen
    connections = []
    for conn in list_with_connections:
        if station[0] == conn.station1 or station[0] == conn.station2:
            connections.append(conn)
            if boolean:
                conn.setCritic(boolean)
                
    list_with_stations.append(STATION(station[0], boolean, connections, station[2], station[1]))

if OPDRACHT == "1h":
    for conn in list_with_connections:
        if conn.station1 in utrechtjes and conn.station2 in utrechtjes:
            conn.setCritic(True)


" OPSTELLEN LIJNVOERING "

maximum_doelwaarde = 0

# Loop voor alle combinaties aantal trajecten/minuten
for treinen in range(MIN_TREINEN, MAX_TREINEN + 1):
    for minuutjes in range(MIN_MINUTEN, MAX_MINUTEN + 1):
        
        # Restricties lijnvoering
        MAX_AANTAL_TREINEN = treinen
        MAX_AANTAL_MINUTEN = minuutjes
        
        # Indien er sprake is van random keuzes, vaker uitvoeren
        for AantalKeerLoopen in range(aantalLoops):
            
            # Zet alle connecties op unused
            for conn in list_with_connections:
                conn.used = False
                  
            # Opstellen trajecten (Ken alleen de 1e connectie toe)
            list_with_trajects = []  
            while len(list_with_trajects) < MAX_AANTAL_TREINEN:
                # aanroepen functie new_traject voor opstellen traject
                new = new_traject(list_with_connections, TRAJECT_OPSTELLEN)
                if new != False:
                    list_with_trajects.append(new)
                else:
                    break
            
            # Ieder traject per stuk maximaal uitbreiden
            for traject in list_with_trajects:
                # aanroepen methode new_connection voor uitbreiden traject
                while True: 
                    if not traject.new_connection(list_with_connections, MAX_AANTAL_MINUTEN, TRAJECT_UITBREIDEN):
                        break
                 
                    
            # Als er nog kritieke sporen ongebruikt zijn, probeer deze toe te voegen mbv linken-functie
            for i in list_with_connections:   
                if i.used == False and i.critic == True:
                    if linken([i.station1, i.station2], i.duration, list_with_trajects, list_with_stations, MAX_AANTAL_MINUTEN, doelfunctie(list_with_connections, list_with_trajects), list_with_connections, list_with_connections.index(i)):
                        i.setUsed(True)
            
            
            
            # Alle coördinaten van ongebruikte kritieke sporen opslaan
            x_unused = []
            y_unused = []
            for i in list_with_connections: 
                if i.used == False and i.critic == True:  
                    # Per connectie 2 x-waardes en 2 y-waardes opslaan
                    x = []
                    y = []
                    for s in list_with_stations:
                        if s.name in [i.station1, i.station2]:
                            x.append(float(s.x))
                            y.append(float(s.y))
                    x_unused.append(x)
                    y_unused.append(y)
                   
            # Vergelijk kwaliteit van huidige lijnvoering met best gevonden lijnvoering
            doel = doelfunctie(list_with_connections, list_with_trajects)
            if doel >= maximum_doelwaarde:
                maximum_doelwaarde = doel
                treinen_save = treinen
                minuten_save = minuutjes
                trajecten_save = deepcopy(list_with_trajects)
                connecties_save = deepcopy(list_with_connections)
                x_unused_save = x_unused
                y_unused_save = y_unused




" BEST GEVONDEN LIJNVOERING OPTIMALISEREN "

print("Kwaliteit voor optimaliseren: " + str(maximum_doelwaarde))    
print("")

list_with_trajects = deepcopy(trajecten_save)
list_with_connections = deepcopy(connecties_save)

# Aanroepen hill climbing functie
for i in range(1000):
    resultaat = hill_climbing(list_with_trajects, list_with_stations, list_with_connections)
    if resultaat != False:
        list_with_trajects = deepcopy(resultaat[0])
        list_with_connections = deepcopy(resultaat[1])

# Aanroepen simulates annealing functie
for i in range(1000):
    resultaat = simulated_annealing(list_with_trajects, list_with_stations, list_with_connections, i)
    if resultaat != False:
        list_with_trajects = deepcopy(resultaat[0])
        list_with_connections = deepcopy(resultaat[1])




" PRINTEN EN PLOTTEN RESULTAAT "

xen = []
yen = []
# Print alle stations + lengte van alle trajecten                
print("___________TRAJECTEN:___________")
for traject in list_with_trajects:
    print(traject.stations)
    print(traject.total_time)
    print("")
    x = []
    y = []
    
    # Sla ieder de connecties(coördinaten) van ieder traject op
    for station in traject.stations:
        for stat in list_with_stations:
            if stat.name == station:
                x.append(float(stat.x))
                y.append(float(stat.y))
    xen.append(x)
    yen.append(y)


print("Opdracht: " + OPDRACHT)    
print("Aantal trajecten: " + str(treinen_save))
print("Max aantal minuten per traject: " + str(minuten_save))
print("Kwaliteit na optimaliseren: " + str(maximum_doelwaarde))    

# Roep plot functie aan
plotten(OPDRACHT, xen, yen, x_unused_save, y_unused_save)


