customers = ["bilalsevinc", "yunussevinc", "emresevinc", "ahmeterden"]
order_totals = [12000, 13000, 5000, 15000]

# 1- Add an order of 5000 lira made with the username 'sadikturan' to the list.
customers.append("bilalsevinc")
order_totals.append(5000)

# 2- Remove the last added order.
# customers.pop()
# order_totals.pop()

# 3- Print the summary sentence for all customers.
# '<username>' has a total order of '<10000>' lira. (using loops)
result = f"{customers[0]} has a total order of {order_totals[0] + order_totals[4]} lira"
result = f"{customers[1]} has a total order of {order_totals[1]} lira"

# 4- Sort the customers alphabetically.
customers.sort()

# 5- Sort the order totals in descending order.
order_totals.sort()
order_totals.reverse()

# 6- What is the lowest order?
result = min(order_totals)
result = max(order_totals)

# 7- How many orders does the user 'bilalsevinc' have?
result = customers.count('bilalsevinc')

# 8- Remove the user 'ahmeterden' from the customers list.
customers.remove('ahmeterden')

# 9- Clear all contents from the lists.
# customers.clear()
# order_totals.clear()

# 10- Add the username and order totals received from the user to the list.
username = input('Customer name: ')
total = input('Total: ')
customers.append(username)
order_totals.append(total)

print(customers)
print(order_totals)

# Output:

"""

Customer name: ismail
Total: 500
['bilalsevinc', 'bilalsevinc', 'emresevinc', 'yunussevinc', 'ismail']
[15000, 13000, 12000, 5000, 5000, '500']

"""