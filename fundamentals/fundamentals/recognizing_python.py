num1 = 42 #number
num2 = 2.3 #numbers
boolean = True #boolean
string = 'Hello World' #strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, list, access value
pizza_toppings.append('Mushrooms') #list, remove value
print(person['name']) #log statement, dictionary, access value
person['name'] = 'George' #dictionary, add value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2]) #log statement, list, access value

if num1 > 45: #conditional, if
    print("It's greater")
else: #conditional, else
    print("It's lower")

if len(string) < 5: #conditional, if
    print("It's a short word!")
elif len(string) > 15: #conditional, else if
    print("It's a long word!")
else: #conditional, else
    print("Just right!")

for x in range(5): #start
    print(x)
for x in range(2,5): 
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) # list, delete value

print(person) #log statement
person.pop('eye_color') #list delete value
print(person) #log statement

for topping in pizza_toppings: 
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #function

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #function
print_hello_x_or_ten_times(4) #function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)