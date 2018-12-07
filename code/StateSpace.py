import os
import csv

def statespace():
    " 'ConnectiesHolland.csv' voor noord+zuid-holland, 'ConnectiesNationaal.csv' voor heel nl "
    naam_connecties = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'code', 'csv', 'ConnectiesNationaal.csv')
    bestand_connecties = open(naam_connecties, encoding='utf-8-sig')
    all_connections = csv.reader(bestand_connecties)
    
    stations = []
    connecties = {}
    
    for line in all_connections:
        if line[0] not in stations:
            stations.append(line[0])
            connecties[line[0]] = {line[1]: float(line[2])}
        else:
            connecties[line[0]][line[1]] = float(line[2])
            
        if line[1] not in stations:
            stations.append(line[1])
            connecties[line[1]] = {line[0]: float(line[2])}
        else:
            connecties[line[1]][line[0]] = float(line[2])
    
    # afgemaakte trajecten
    lijst1 = []
    
    afstanden1 = []
    
    for stad in range(len(stations)):
    
        # moeten uitgebreid worden
        lijst2 = [[stations[stad]]]
        # uitgebreide trajecten
        lijst3 = []
        
        afstanden2 = [0]
        afstanden3 = []
        
        while lijst2:
            verwijderen = []
            # alle trajecten in lijst 2 afgaan
            for i in range(len(lijst2)):
                
                len3 = len(lijst3)
        
                # alle connecties van eind station in traject afgaan
                for j in connecties[lijst2[i][-1]]:
                    
                    if len(lijst2) > 1:
                        
                        # is connectie niet als laatste connectie gebruikt? niet teruggaan over zelfde spoor
                        if j != lijst2[i][-2]:
                            # is lengte nieuw traject toegestaan?
                            " 120 voor noord+zuid-holland, 180 voor heel nl "
                            if afstanden2[i] + connecties[lijst2[i][-1]][j] <= 180:
                                # huidig traject kopieeren
                                t = lijst2[i][:]
                                # connectie toevoegen
                                t.append(j)
                                # nieuwe traject opslaan
                                lijst3.append(t)
                                
                                afstanden3.append(afstanden2[i] + connecties[lijst2[i][-1]][j])
                    else:
                        
                        # is lengte nieuw traject toegestaan?
                        " 120 voor noord+zuid-holland, 180 voor heel nl "
                        if afstanden2[i] + connecties[lijst2[i][-1]][j] <= 180:
                            # huidig traject kopieeren
                            t = lijst2[i][:]
                            # connectie toevoegen
                            t.append(j)
                            # nieuwe traject opslaan
                            lijst3.append(t)
                            
                            afstanden3.append(afstanden2[i] + connecties[lijst2[i][-1]][j])
                
                if len3 == len(lijst3):
                    #traject i is niet uitbreidbaar -> verplaatsen naar lijst1
                    
                    verwijderen.append(i)
                           
            for verwijder in reversed(verwijderen):
                # komst laatste stad eerder in stations list dan beginstation?: niet toevoegen, alleen verwijderen
                laatste = stations.index(lijst2[verwijder][-1])
                eerste = stations.index(lijst2[verwijder][0])
                if laatste >= eerste:
                    lijst1.append(lijst2[verwijder][:])
                    afstanden1.append(afstanden2[verwijder])
                del lijst2[verwijder]
                del afstanden2[verwijder]
                    
            lijst2 = lijst3[:]
            lijst3 = []
            
            afstanden2 = afstanden3[:]
            afstanden3 = []
        
    return([lijst1, afstanden1])
