
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

#exportfile = open('export.csv', 'a')


OPDRACHT = "1e"  # "1a", "1b", "1c"
TRAJECT_OPSTELLEN = "random"  # "min", "max", "random"
TRAJECT_UITBREIDEN = "random"  # "min", "max", "random"

if TRAJECT_OPSTELLEN == "random" or TRAJECT_UITBREIDEN == "random":
    aantalLoops = 5000
else:
    aantalLoops = 1

if OPDRACHT == "1a":
    MIN_TREINEN = 4
    MAX_TREINEN = 4
    MIN_MINUTEN = 120
    MAX_MINUTEN = 120
elif OPDRACHT == "1b" or OPDRACHT == "1c":
    MIN_TREINEN = 4
    MAX_TREINEN = 4
    MIN_MINUTEN = 100
    MAX_MINUTEN = 100
elif OPDRACHT == "1d":
    MIN_TREINEN = 9
    MAX_TREINEN = 9
    MIN_MINUTEN = 180
    MAX_MINUTEN = 180
elif OPDRACHT == "1e":
    MIN_TREINEN = 12
    MAX_TREINEN = 12    
    MIN_MINUTEN = 180
    MAX_MINUTEN = 180

bestanden = importeren(OPDRACHT)
all_connections = bestanden[0]
all_stations = bestanden[1]

" PUT ALL CONNECTIONS LIKE CONNECTION OBJECT IN LIST "
list_with_connections = []
for connection in all_connections:
    list_with_connections.append(CONNECTION(connection[0], connection[1], float(connection[2])))
   

" PUT ALL STATIONS LIKE STATION OBJECT IN LIST "
list_with_stations = []
for station in all_stations:
    if station[-1] == "Kritiek" or OPDRACHT in ["1c", "1e"]:
        boolean = True
    else:
        boolean = False

    connections = []
    for conn in list_with_connections:
        if station[0] == conn.station1 or station[0] == conn.station2:
            connections.append(conn)
            if boolean:
                conn.setCritic(boolean)
    list_with_stations.append(STATION(station[0], boolean, connections, station[2], station[1]))

maximum_doelwaarde = 0

for treinen in range(MIN_TREINEN, MAX_TREINEN + 1):
    for minuutjes in range(MIN_MINUTEN, MAX_MINUTEN + 1):
        
        " RESTRICTIES LIJNVOERING "
        MAX_AANTAL_TREINEN = treinen
        MAX_AANTAL_MINUTEN = minuutjes
        
        for AantalKeerLoopen in range(aantalLoops):
#            exportfile.write("-----------------------------------  NIEUW  -----------------------------\n")
#            exportfile.write(str(MAX_AANTAL_TREINEN) + "   " + str(MAX_AANTAL_MINUTEN) + "\n")
#            exportfile.write("\n")
            
            for conn in list_with_connections:
                conn.used = False
                  
            " CREATE X AMOUNT OF TRAJECTS "
            list_with_trajects = []  
            while len(list_with_trajects) < MAX_AANTAL_TREINEN:
                # aanroepen functie new_traject voor opstellen traject
                new = new_traject(list_with_connections, TRAJECT_OPSTELLEN)
                if new != False:
                    list_with_trajects.append(new)
#                    exportfile.write(str(new.stations) + "     " + str(new.total_time) + "\n")
                else:
                    break
            
            " per traject helemaal opstellen "
            for traject in list_with_trajects:
                # aanroepen methode new_connection voor uitbreiden traject
                while True: 
                    if not traject.new_connection(list_with_connections, MAX_AANTAL_MINUTEN, TRAJECT_UITBREIDEN):
                        break
            
            " per traject telkens maar 1 connectie toevoegen "
#            grens = [True] * len(list_with_trajects)
#            
#            while True in grens:
#                for i in range(0, len(list_with_trajects)):
#                    if grens[i] == True:
#                        if not list_with_trajects[i].new_connection(list_with_connections, MAX_AANTAL_MINUTEN, TRAJECT_UITBREIDEN):
#                            grens[i] = False
                 
                    
            " TRY TO ADD UNUSED CRITIC CONNECTIONS TO EXISTING TRAJECTS "
            for i in list_with_connections:   
                if i.used == False and i.critic == True:
                    if linken([i.station1, i.station2], i.duration, list_with_trajects, list_with_stations, MAX_AANTAL_MINUTEN):
                        i.setUsed(True)
            
#            exportfile.write("\n")
            " PRINT UNUSED CONNECTIONS " 
            aantal = 0
            for i in list_with_connections: 
                if i.used == False and i.critic == True:    
                    aantal += 1
#                    exportfile.write(i.station1 + "  -  " + i.station2 + "\n")
                   
            
#            exportfile.write("\n")
#            for traject in list_with_trajects:
#                exportfile.write(str(traject.stations) + "    " + str(traject.total_time) + "\n")
                
#            exportfile.write("\n")
#            exportfile.write("Doelwaarde: \n")
#            exportfile.write(str(doelfunctie(list_with_connections, list_with_trajects)) + "\n")
#            exportfile.write(str(aantal) + "\n")
#            exportfile.write("\n")
            
            doel = doelfunctie(list_with_connections, list_with_trajects)
            if doel >= maximum_doelwaarde:
                maximum_doelwaarde = doel
                treinen_save = treinen
                minuten_save = minuutjes
                aantal_save = aantal
                trajecten_save = deepcopy(list_with_trajects)
                connecties_save = deepcopy(list_with_connections)


list_with_trajects = deepcopy(trajecten_save)
list_with_connections = deepcopy(connecties_save)

xen = []
yen = []
" PRINT & PLOT BEST FINAL TRAJECTS "                   
print("___________TRAJECTEN:___________")
for traject in list_with_trajects:
    print(traject.stations)
    print(traject.total_time)
    print("")
    x = []
    y = []
    for station in traject.stations:
        for stat in list_with_stations:
            if stat.name == station:
                x.append(float(stat.x))
                y.append(float(stat.y))
    xen.append(x)
    yen.append(y)


print(OPDRACHT)    
print(treinen_save)
print(minuten_save)
print(maximum_doelwaarde)     
print(aantal_save)

plotten(OPDRACHT, xen, yen)

for i in range(100):
    resultaat = hill_climbing(list_with_trajects, list_with_stations, list_with_connections)
    if resultaat != False:
        list_with_trajects = deepcopy(resultaat)
        
#exportfile.close() 
print(doelfunctie(list_with_connections, list_with_trajects))