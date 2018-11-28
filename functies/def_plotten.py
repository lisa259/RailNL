" PLOTTEN "

import matplotlib.pyplot as plt

def plotten(OPDRACHT, x_punten, y_punten):
    if OPDRACHT in ["1a", "1b", "1c"]:
        x_min = 51.80722046 - 0.1
        x_max = 52.95527649 + 0.1       # 1,14805603
        y_min = 4.324999809 - 0.07
        y_max = 5.055555344 + 0.07      # 0,730555535
    elif OPDRACHT in ["1d", "1e", "1f"]:
        x_min = 50.85027695 - 0.23
        x_max = 53.21055603 + 0.23      # 2,36027908
        y_min = 3.595277786 - 0.32
        y_max = 6.889999866 + 0.32      # 3,2947222126
    
    plt.axis([x_min, x_max, y_min, y_max])
    
    #plt.plot([52.34666824, 52.38777924, 52.16611099, 52.08027649], [4.917778015, 4.638333321, 4.481666565, 4.324999809], 'ro')
    for i in range(len(x_punten)):
        plt.plot(x_punten[i], y_punten[i])
    plt.show()
    
#plotten("1a", [[52.34666824, 52.38777924], [52.16611099, 52.08027649]], [[4.917778015, 4.638333321], [4.481666565, 4.324999809]])