print("""This will calculate the shipping cost depending on the weight and if
we use ground, drone or premium shipping.""")

def ground_shipping_cost(weight):
  if weight <= 2:
    cost = 1.50 * weight
  elif weight <= 6:
    cost = 3.00 * weight
  elif weight <= 10:
    cost = 4.00 * weight
  else:
    cost = 4.75 * weight
  return cost + 20

premium_cost = 125

def drone_shipping_cost(weight):
  if weight <= 2:
    cost = 4.50 * weight
  elif weight <= 6:
    cost = 9.00 * weight
  elif weight <= 10:
    cost = 12.00 * weight
  else:
    cost = 14.25 * weight
  return cost 

print("The price with ground shipping for 8.4 lbs is $" + str(ground_shipping_cost(8.4)))
print("The price with drone shipping for 1.5 lbs is $" + str(drone_shipping_cost(1.5)))
print("The price for premium ground is $" + str(premium_cost))

def cheapest(weight):
  if drone_shipping_cost(weight) <= ground_shipping_cost(weight) and drone_shipping_cost(weight) <= premium_cost:
    return "Cheapest is drone shipping $" + str(drone_shipping_cost(weight))
  elif ground_shipping_cost(weight) <= drone_shipping_cost(weight) and ground_shipping_cost(weight) <= premium_cost:
    return "Cheapest is ground shipping $" + str(ground_shipping_cost(weight))
  else:
    return "Cheapest is premium shipping $" + str(premium_cost)

print("For 4.8 lbs " + cheapest(4.8))

print("For 41.5 lsb " + cheapest(41.5))

