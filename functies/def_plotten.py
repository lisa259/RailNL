" PLOTTEN "

import matplotlib.pyplot as plt

def plotten(OPDRACHT, x_punten, y_punten, x_unused, y_unused):
    if OPDRACHT in ["1a", "1b", "1c"]:
        y_min = 51.80722046 - 0.1
        y_max = 52.95527649 + 0.1       # 1,14805603
        x_min = 4.324999809 - 0.07
        x_max = 5.055555344 + 0.07      # 0,730555535
    elif OPDRACHT in ["1d", "1e"]:
        y_min = 50.85027695 - 0.23
        y_max = 53.21055603 + 0.23      # 2,36027908
        x_min = 3.595277786 - 0.32
        x_max = 6.889999866 + 0.32      # 3,2947222126
    
    plt.axis([x_min, x_max, y_min, y_max])
    
    for i in range(len(x_punten)):
        plt.plot(x_punten[i], y_punten[i])
        
    for i in range(len(x_unused)):

        plt.plot(x_unused[i], y_unused[i], 'k:')
        
    plt.show()
    
#plotten("1a", [[52.00666809, 52.08027649, 52.16611099, 52.08027649, 52.01750183]], [[4.356389046, 4.324999809, 4.481666565, 4.324999809, 4.704444408]])