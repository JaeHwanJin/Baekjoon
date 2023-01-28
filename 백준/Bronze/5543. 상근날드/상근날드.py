burger = []
drink = []

for i in range(3) :
    price = int(input())
    burger.append(price)
for i in range(2) :
    price = int(input())
    drink.append(price)

print(min(burger) + min(drink) - 50)