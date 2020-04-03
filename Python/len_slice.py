
print{"""This program will help organize the pizzas listing 
from a restaurant and some sales datas.""" }
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
pizzas = list(zip(prices, toppings))
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza  = pizzas[num_pizzas - 1]
print("The priciest pizza is " + str(priciest_pizza))
three_cheapest = pizzas[:3]
print("The 3 cheapest pizzas are " + str(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
