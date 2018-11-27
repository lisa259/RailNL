
" BEPALEN KWALITEIT VAN LIJNVOERING "       
def doelfunctie(list_with_connections, list_with_trajects):
    # bepalen p
    aantalkritiek = 0
    aantalgebruikt = 0
    for connection in list_with_connections:
        if connection.critic:
            aantalkritiek += 1
            if connection.used:
                aantalgebruikt += 1
    p = aantalgebruikt / aantalkritiek
    
    T = len(list_with_trajects)
    
    # bepalen Min
    Min = 0
    for traject in list_with_trajects:
        Min += traject.total_time
    
    return (p * 10000 - T * 20 - Min / 10)