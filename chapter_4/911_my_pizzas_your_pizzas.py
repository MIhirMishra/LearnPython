pizzas = ['cheese pizza', 'thin crust veggie', 'thin crust chicken']
friend_pizza = pizzas[:]
pizzas.append('chicken pizza')
friend_pizza.append('chicken pineapple pizza')
print('My favourite pizzas are:\n' + str(pizzas))
print("My friend's favourite pizzas are:\n" + str(friend_pizza))