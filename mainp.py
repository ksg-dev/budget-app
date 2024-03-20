# This entrypoint file to be used in development. Start by reading README.md
import practice
from practice import create_spend_chart
#from practice import chart
#from unittest import main

food = practice.Category("Food")
business = practice.Category("Business")
entertainment = practice.Category("Entertainment")
"""
food.deposit(1000, "initial deposit")
food.deposit(100, "test1")
food.deposit(10)
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = practice.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = practice.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.deposit(130, "test")
auto.withdraw(15)
food.transfer(50, auto)

print(food)
print(auto)
print(clothing)

print('--------')

print(create_spend_chart([food, clothing, auto]))
"""

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])

print(actual)
print(repr(actual))

#print(chart([5,4,1]))

# Run unit tests automatically
#main(module='test_module', exit=False)