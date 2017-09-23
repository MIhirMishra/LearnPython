pizzas = ['cheese pizza', 'thin crust veggie', 'thin crust chicken']
friend_pizza = pizzas[:]
pizzas.append('chicken pizza')
friend_pizza.append('chicken pineapple pizza')

for pizza in pizzas:
    print('My pizza: ' + pizza)
for pizza in friend_pizza:
    print('Friend pizza: ' + pizza)
