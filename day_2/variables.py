# Day 2:30 days of python programming
from filecmp import cmp
import math


first_name = 'Maisara'
last_name = 'Lweno'
full_name = first_name + ' ' + last_name
country = 'Tanzania'
city = 'Dar es Salaam'
age = 20
year = 2026
is_married = False
is_true = False
is_light_on = True
print(first_name,last_name,full_name,country,city,age,year,is_married,is_true,is_light_on)

# exercise 2 of Day2.
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
print(len(last_name))
print(len(first_name),len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one- num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one/num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one**num_two
print(exp)
floor_division = num_one//num_two
print(floor_division)
radius = 30
area_of_circle = math.pi * radius**2
circumference_of_the_circle = 2 * math.pi *radius
print(area_of_circle)
print(circumference_of_the_circle)


