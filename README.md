# Heuristieken
## RailNL

### Lower- en upperbounds
  
De doelfunctie voor de kwaliteit van de lijnvoering geldt als volgt:
K = p * 10000 - T * 20 - Min / 10    (waarbij K=kwaliteit, p = fractie gebruikte kritieke sporen, t = aantal treinen, Min = aantal minuten)
  
De lowerbound wordt bereikt wanneer:
- Geen enkel kritiek spoor bereden wordt (p = 0).
- Het maximum aantal treinen wordt ingezet.
- Het maximum aantal minuten (per traject) wordt bereikt.
  
De upperbound wordt bereikt wanneer:
- Ieder kritiek spoor bereden wordt (p = 1).
- Zo min mogelijk treinen worden ingezet.
- Zo min mogelijk minuten worden gebruikt.
  
**1a/b.** 
> lowerbound:  
p = 0    
t = 7  
Min = 7 * 120   
K = 0 * 1000 - 7 * 20 - 7 * 120 / 10 = -224       
        
> upperbound:      
p = 1      
t = 287 / 120 omhoog afronden = 3        
Min = 287       
K = q * 1000 - 3 * 20 - 287 / 10 = 9911,3  
       
**1c.**  
> lowerbound:  
p = 0
t = 7  
Min = 7 * 120   
K = 0 * 1000 - 7 * 20 - 7 * 120 / 10 = -224  

> upperbound:      
p = 1      
t = 381 / 120 omhoog afronden = 4       
Min = 381       
K = q * 1000 - 4 * 20 - 381 / 10 = 9881,9  

