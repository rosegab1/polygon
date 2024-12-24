#Gabriela Feliciano
#U60146452
'''The purpose of this program is to output the area and perimeter
of a polygon depending on the number of sides and length of the sides
inputted by the user'''

import math

class Polygon:
    def __init(self):
        self.__sides = int(0)
        self.__length = float(0.0)


#----accessor methods-------
    def getsides(self):
        return self.__sides

    def getlength(self):
        return self.__length

#------mutator methods---------
    def setsides(self, n):
        self.__sides = n

    def setlength(self, l):
        self.__length = l

#-------additional methods------
    def perimeter(self, n, l):
        return self.__sides * self.__length

    def area(self, n, l):
        return self.__sides * (self.__length **2) / 4 / math.tan(math.pi / self.__sides)


def main():
    shape = Polygon()
    num_sides = int(input('Enter the number of sides (>=3): '))
    while num_sides < 3:
        num_sides = int(input('Invalid entry. Re-enter the number of sides (>=3): '))
    length_sides = float(input('Enter the length of each sides (>=0.1): '))
    while length_sides < 0.1:
        length_sides = float(input('Invalid entry. Re-enter the length of each side (>=0.1): '))
    shape.setsides(num_sides)
    shape.setlength(length_sides)
    print(f'The polygon has {num_sides} sides. Each side is {length_sides} units in length.\nThe perimeter of the polygon is {shape.perimeter(num_sides, length_sides):,.3f} units and its area is {shape.area(num_sides, length_sides):,.3f} square units.')

main()
