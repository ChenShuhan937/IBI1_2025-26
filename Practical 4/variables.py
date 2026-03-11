#Scotland population calculation
#Populationin2004 (millions)
a=5.08
#Population in 2014 (millions)
b=5.33
#Population in 2024 (millions)
c=5.55
#Population change 2004-2014
d=b-a
#Population change 2014-2024
e=c-b
#Compare the size of d and e
print("Population change 2004-2014:",d)
print("Population change 2014-2024:",e) 
print("Is d greater than e:",d>e)
#d=0.25, e=0.22. e<d, growth slow down
#Scotland's population growth is  slowing down: the population increase from 2014-2024 is less than that from 2004-2014.
<<<<<<< HEAD
#comment: the population growth is decelerating.
=======
#population growth is decelerating.
>>>>>>> 0cb361772a17d6ff6a6c790f55ca65e0540439d0
#4.2 Boolean operations
#Define boolean variables X and Y
X=True
Y=False
#Calculate X or Y and assign to W
W=X or Y
#print the result of W
print("Result of W=X or Y:",W)
#True table for W
#X=True,Y=True -> W=True
#X=True,Y=False -> W=True
#X=False, Y=True -> W=True
#X=False, Y=False -> W=False
