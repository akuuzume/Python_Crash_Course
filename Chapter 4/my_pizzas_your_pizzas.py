my_pizzas = ['pepporini','chicken','peri peri']
friends_pizza = my_pizzas[:]
my_pizzas.append('cheese')
friends_pizza.append('beef')

print("My favourite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favourite pizzas are: ")
for pizza in friends_pizza:
    print(pizza)
