APPLES = .50
BREAD = 1.50
CHEESE = 2.25
numApples = 3
numBread = 10
numCheese = 6
prcApples = numApples * APPLES
prcBread = numBread* BREAD
prcCheese = numCheese * CHEESE
strApples = 'Apples'
strBread = 'Rye Bread'
strCheese = 'Cheese'
total = prcBread + prcCheese + prcApples
print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples:10s}{numApples:10d}{"":5s}${prcApples:>5.2f}')
print(f'{strBread:10s}{numBread:10d}{"":5s}${prcBread:>5.2f}')
print(f'{strCheese:10s}{numCheese:10d}{"":5s}${prcCheese:>5.2f}')
print(f'{"":10s}{"Total:":>10s}{"":5s}${total:>5.2f}')