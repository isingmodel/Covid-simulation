
The purpose of this work
* proof SIQR model is working and make sense. 
* correlation between disease contagion and
  population size of each social meeting 


Rules
1. It is a semi-mean field model -> no? yes?
2. SIQR model
   (susceptible, Quarantined, infectious, recovered)
3. People meet each other with group.
4. the size of the groups varies. 2,3,4...
5. the rate to meet ezach other is 
   in proportion to the distance(not linear)
6. the distance among population means their difference
   of index number
7. the size of each group meeting is random, but 
   decreases when the total number of infectious is large
8. (do later) total number of people who meet other people decreases 
   when the total number of infectious is large.
9. If there are infectious in the group meetings, susceptible in the group
   got probability to be exposed. 
10. when infectious peoples detected, the group of people they met
    are converted to Quarantined state. 
11. also, the detected Infectious are also be quarantined. 
12. so, there are two types of quarantined people.  
    susceptible-Quarantined, and infectious-Quarantined. 



Algorithm
1. the day start
2. making groups. size 2 to X (should make algorithm)
3. In one day, one person can participate one group
4. for each group, if there are infectiouses, calculate 
   susceptible -> exposed
5. day end
6. after day end, perform I -> R (this speed is consistant)
7. after day end, perform S -> I (this speed is consistant)
8. every day infectiouses have chance to be detected by quarantine authorities.(fixed rate)
9. Detected infectiouses are quarantined and cannot
   get into social group before they converted into R
