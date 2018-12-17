" PLOTTEN "

import matplotlib.pyplot as plt

def plotten(OPDRACHT, x_punten, y_punten, x_unused, y_unused):
    # Grenzen x en y as bepalen
    if OPDRACHT in ["1a", "1b", "1c"]:
        y_min = 51.7
        y_max = 53
        x_min = 4.25
        x_max = 5.1     
    elif OPDRACHT in ["1d", "1e", "1h"]:
        y_min = 50.6
        y_max = 53.45
        x_min = 3.25
        x_max = 7.2    
    
    plt.axis([x_min, x_max, y_min, y_max])
   
    # plot de trajecten
    for i in range(len(x_punten)):
        plt.plot(x_punten[i], y_punten[i])
      
    # plot ongebruike connecties
    for i in range(len(x_unused)):
        plt.plot(x_unused[i], y_unused[i], 'k:')
        
    plt.show()
