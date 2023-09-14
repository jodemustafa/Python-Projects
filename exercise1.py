# u4133726 jode mustafa

# tis program will take the input from a user about number of sides and length of eeach side and calculate it using defined functions and classes

import math 

class polygon:
    def __init__(self):
        self.__s=0
        self.__l=0.0


    def getnumberofsides(self):
        return self.__s

    def getlength(self):
        return self.__l

    def setsides(self,s):
        self.__s= s


    def setlength(self,l):
        self.__l = l

    def perimeter(self):
       return self.__s*self.__l

    def area(self):
        pi=float(math.pi)
        return(self.__s*(self.__l**2)) / (4*(math.tan((math.pi)/self.__s)))

def main():
        polygon2 = polygon()
        
        s= int(input("enter number of sides (>=3)  "))
        if s <3:
            s=int(input("invalid entry. re-enter number of sides  "))

        l= float(input("enter the length of each side:  "))
        if l<0.1:
            l=float(input(" invalid entry re-enter the value "))


        polygon2.setsides(s)
        polygon2.setlength(l)

        print(f'the polygon2 has {polygon2.getnumberofsides()} sides each side is {polygon2.getlength()} units in length')
        print(f"the perimeter of the polygon2 {polygon2.perimeter():.3f} units and it's area is {polygon2.area():.3f} square units")

main()