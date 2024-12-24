#Gabriela Feliciano
#U60146452
'''The purpose of this program is to provide a summary of two
items that the user has inputted which includes the type of item, the amount,
and the price.'''

class Retail_Item:
    def __init__(self, t, a, p):
        self.__type = t
        self.__amount = a
        self.__price = p

    def __str__(self):
        return f'{self.__type:20}{self.__amount:18}${self.__price}'

def main():
    item1 = Retail_Item((t := input('Name of item 1: ')), (a:= input('Amount of item 1: ')), (p := input('Price of item 1: ')))
    print()
    item2 = Retail_Item((t := input('Name of item 2: ')), (a:= input('Amount of item 2: ')), (p := input('Price of item 2: ')))
    print()

    print('Here is a summary of the items you added:')
    print(f'{"Item":20}{"Amount":18}{"Price"}')
    print('-'*44)
    print(item1.__str__())
    print(item2.__str__())

main()
