num1 = 42   # variable declaration, primitive data types: number
num2 = 2.3  # variable declaration, primitive data types: number
boolean = True # variable declaration, primitive data types: boolean
string = 'Hello World' # variable declaration, primitive data types: string

# variable declaration, initialize list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration, initialize dictionary, string, number, boolean, 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable declaration, initialize tuple
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  # log statement, type check
print(pizza_toppings[1])    # log statement, access list value
pizza_toppings.append('Mushrooms')  # add list value
print(person['name'])   # access dictionary value
person['name'] = 'George'   # change dictionary value
person['eye_color'] = 'blue'    # add dictionary value    
print(fruit[2]) # log statement, access tuple value

# if, else if, and else conditional statements, log statements
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# string length check
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loops, number, increment, log statements
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):  # while loop
    print(x)    # log statement
    x += 1  # change value


pizza_toppings.pop()    # list delete value
pizza_toppings.pop(1)   # list delete value

print(person)   # log statement
person.pop('eye_color') # delete dictionary value
print(person)   # log statement

for topping in pizza_toppings:  # for loop, 
    if topping == 'Pepperoni':  # if statement, argument
        continue    # continute
    print('After 1st if statement') #log statement
    if topping == 'Olives': # if statement, argument
        break   # break

def print_hello_ten_times():    # function
    for num in range(10):   # for loop, number, increment for loop
        print('Hello')  # log statement

print_hello_ten_times() # function call

def print_hello_x_times(x): # function, parameter 'x'
    for num in range(x):    # for loop, argument 'x', number, increment for loop
        print('Hello')  # log statement

print_hello_x_times(4)  # function call

def print_hello_x_or_ten_times(x = 10): # function paramenter, argument
    for num in range(x):    # for loop, number, increment
        print('Hello')  # log statement

print_hello_x_or_ten_times()    # function call
print_hello_x_or_ten_times(4)   # function call


"""
Bonus section
"""

# print(num3)   # NameError: name 'num3' is not defined
# num3 = 72 
# fruit[0] = 'cranberry'    # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    # KeyError: 'favorite_team'
# print(pizza_toppings[7])  # IndexError: list index out of range
#   print(boolean)  # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'appen'
# fruit.pop(1)  # AttributeError: 'tuple' object has not attribute 'pop'