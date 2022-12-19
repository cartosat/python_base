from array import *


def ev_od(list):
    ev=0
    od=0

    for j in list:
        if j%2==0:
            ev+=1
            eva=array('i',[])
            eva.append(j)

        else:
            od+=1

    print("Even:-",ev,eva)
    print("Odd:-",od)



list=[1,2,3,4,5,6,7,8,9,10]

ev_od(list)