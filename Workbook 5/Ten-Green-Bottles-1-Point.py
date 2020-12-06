#Ten green bottles problem 

#imports
import time
#subroutine to output 10 green bottles song

def Greenbottles(bottles):

  for x in range(bottles,0,-1):

    print("{} Green bottles hanging on the wall,\n{} Green bottles hanging on the wall,\nAnd if one green bottle should accidentally fall\nThere'll be {} green bottles hanging on the wall,".format(x,x,x-1))
    time.sleep(1)


#main program

bottles = int(input("How many bottles are on the wall? \n :"))

Greenbottles(bottles)