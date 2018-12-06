#Heuristieken project
## Case RailNL

De opdrachten zijn als volgt:
1a) Stel een lijnvoering op voor Noord- en Zuid-Holland met maximaal 7 trajecten waarbij alle trajecten binnen
    120 minuten gereden moeten worden en alle kritieke verbindingen moeten bereden worden.
1b) Optimaliseer het antwoord van a met behulp van de volgende formule:

> (maximaliseer) K = p*10000 - (T*20 + Min/10

> p = fractie van hoeveel kritieke verbindingen bereden worden

> T = aantal treinen (trajecten)

> Min = tijdsduur van alle treinen samen in minuten


1c) Ga er nu vanuit dat alle verbindingen kritiek zijn. Hoe hoog kun je K maken?

1d) Maak een lijnvoering voor heel Nederland met maximaal 20 trajecten waarbij alle trajecten binnen
    180 minuten gereden moeten worden en alle kritieke verbinden moeten bereden worden. Met K zo hoog mogelijk.
1e) Doe hetzelfde waarbij je alle verbindingen voor kritiek houd.

## Lower- and Upperbound

1b) Lowerbound:

> We gaan ervan uit dat nul kritieke verbindingen worden bereden. Het maximaal aantal trajecten/treinen wordt ingezet. Dus 7. Deze rijden het maximaal aantal minuten dus 120. Dus kom je op een totaal tijd van 840. Wat betekend dat de waarde van de doelfunctie zo wordt: K = 0*10000 - (7*20 + 840/10) = -224.

Upperbound:

> We gaan ervan uit dat alle kritieke verbindingen bereden worden. De tijd van alle kritieke sporen bij elkaar is 287. Voor 287 minuten zijn minimaal 3 treinen nodig 287/120 > 2. Dus wordt de waarde van de doelfunctie: K = 1*10000 - (3*20 + 287/10) = 9911,3. 

1c) Lowerbound:

> K = 0*10000 - (0*20 + 0/10) = 0.

Upperbound:

> K = 1*10000 - (4*20 + 381/10) = 9881,9.

1d) Lowerbound:

> 

Upperbound:

>

1e) Lowerbound:

>

Upperbound:

>


## State-space 
Bij 1a/b/c is het aantal trajecten dat gemaakt kan worden 2737. Deze trajecten zijn bepaald door vanuit ieder station alle langst mogelijke routes van maximaal 120 minuten op te stellen. Hierbij is het ,tijdens het opstellen van en traject, niet toegestaan om de laatst toegevoegde connectie nog eens toe te voegen. Ook zijn de trajecten die spiegelingen van elkaar zijn, uitgesloten. Omdat er 7 trajecten gebruikt mogen worden is de statespace 7 boven 2737 = 2,265 * 10^20.  

Bij 1d/e is het aantal trajecten van zo lang mogelijke lengte en maximaal 180 minuten dat gemaakt kan worden, is 3761642. Omdat er 20 trajecten gebruikt mogen worden is de statespace 20 boven 3761642 = 1,253* 10^53.  


## Getting Started

### Vereisten
De code is geschreven in Python 3.6. 

### Structuur
Alle in Python geschreven code staat in het mapje code. 

### Test
Om de code te runnen gebruik de volgende instructie:

> In RailNL_main.py voer de opdracht die je wilt uitvoeren in. Ook is er de mogelijkheid om te kiezen welke manier er wordt gebruikt bij zowel het opstellen als het uitbreiden van een traject, hierbij kunt u kiezen uit min, max en random. Run vervolgens het bestand zonder argumenten.


## Auteurs
Lisa Beek en Dorinda van den Dool

## Dankwoord
Minor Programmeren van de UvA.





