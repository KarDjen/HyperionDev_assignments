# initialize items in the coffee shop
menu = ['pain au chocolat', 'croissant', 'juice', 'tart']

# assign the number of stock for each item
stock = {'pain au chocolat': 3,
         'croissant': 9,
         'juice': 34,
         'tart': 14
         }

# assign the price for each item
price = {'pain au chocolat': 2.50,
         'croissant': 2,
         'juice': 3,
         'tart': 4
         }

# initialize variable
total_stock = 0

# find the total value of the stock
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# display the result
print(f'The value of the total stock is {total_stock}.')