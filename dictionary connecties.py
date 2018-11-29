import os
import csv

naam_connecties = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'csv', 'ConnectiesHolland.csv')
bestand_connecties = open(naam_connecties, encoding='utf-8-sig')
all_connections = csv.reader(bestand_connecties)

stations = []
connecties = {}

for line in all_connections:
    if line[0] not in stations:
        stations.append(line[0])
        connecties[line[0]] = {line[1]: line[2]}
    else:
        connecties[line[0]][line[1]] = line[2]
        
    if line[1] not in stations:
        stations.append(line[1])
        connecties[line[1]] = {line[0]: line[2]}
    else:
        connecties[line[1]][line[0]] = line[2]

lijst1 = []
lijst2 = [["Alkmaar"]]
lijst3 = []
afstanden = [[0]]
print(lijst2[-1])
for i in lijst2:
    print(i[-1])
    print(connecties[i[-1]])
    for j in connecties[i[-1]]:
        print(j)
        print(connecties[i[-1]][j])
        t = i
        t.append(j)
        lijst3.append(t)
        afstanden.append(connecties[i[-1]][j])

print(afstanden)