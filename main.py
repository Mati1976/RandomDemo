import numpy as np

Ni=10000; #The Number of itterations
cl=200; #The Length of the random  1/0 array
cs=6; #The Length of identical 1 or 0 we are looking for in the long array
BigCount=0; #The counter for the number of succesful trials 
SmallCount=0; #The counter for the number of tottal successive chains found in all of the 

for z in range (Ni):
    count=0;
    randnums= np.random.randint(0,2,cl)
    #print (randnums)
    for y in range(cl-cs+1):
        Bool1=1;
    
        for x in range(cs-1):
            fp = x+y;
            sp = x+y+1;
            if randnums[fp]==randnums[sp]:
                Bool1=Bool1*1;
            else:
                Bool1=Bool1*0;

        if Bool1==1:
            count=count+1
    #print (count)
    SmallCount=SmallCount+count;
    #print (SmallCount)
    if count !=0:
        BigCount=BigCount+1
print (BigCount/Ni*100) # Printing the precentage of finding a successive chain of cs zeros or ones in a binary random chain of length cl  
print (SmallCount/Ni) # Printing the total of appearnce a successive chain of cs zeros or ones in a binary random chain of length cl  
print (SmallCount/Ni/(cl-cs+1)) #Printing the chance of having a chain of cs zeros or ones in a binary array of the same length 





    