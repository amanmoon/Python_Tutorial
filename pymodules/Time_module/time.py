import time 

def whilel():
    i=0
    while (i<10000):
        print(i)
        i+=1

def forl():
    l=0
    for i in range(10000):
        print(i)


init=time.time()   # this calculate how many sec has passed since 1970 sep 1 
whilel()
time1=(time.time()-init)
init=time.time()   # this calculate how many sec has passed since 1970 sep 1 

forl()
time2=time.time()-init
print(time1)
print(time2)