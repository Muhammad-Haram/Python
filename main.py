# print("Heyyyyy")


# Numbers
a =1 #integer
a = 1.3 #float
a = 22/7 #float
a = 12j #complex
# print(type(a))


# String
st = "Aasjdjsdn$5&*)"
# print(type(st))

# Boolean
t = True
f = False


# indexing
ind = "python"
# print(ind[1])


# string slicing
sl = "python language"

# print(sl[0:6:1])
# print(sl[7::])


# Type convertion
con = 12
con = float(con)
# print(type(con))

bol = -1
bol = bool(bol)
# print(type(bol))
# print(bol)


# formated string / f-string 

name = "haram"
age = 20

# print("my name is ",name, "and my age is ", age) #normal string
# print(f"my name is {name} and my age is {age}") #formated string

# input 

# input_age = int(input("what is your age"))
# print(input_age)
# print(type(input_age))


# operators

# arthmatic operators

num1 = 20.5
num2 = 20

# print(num1 + num2) #add 24
# print(num1 - num2) #sub 16
# print(num1 * num2) #multiplication 80
# print(num1 / num2) #division 5.0
# print(num1 // num2) #floor division 5 "remove decimal values"
# print(num2 ** 3) #Exponentiation "power"
# print(32 % 5) #modulus

#assignment operator

num3 = 20
# num3 = num3 + 40
num3 += 40
num3 -= 20
# print(num3)


# comparsion operator
# < , > , >= , <= , == , !=

# print(num1 == num2)
# print(num1 != num2)
# print(45 > 35)
# print(35 <= 35)

# logical operator 

print(12 < 15 and 12 < 14 or 12 < 14 )

# if/else 

# con = 9
# if con > 10:
#     print(f"{con} is greater then 10")
# else:
#     print(f"{con} is not greater then 10")


# icecream_amount = int(input("please provide me the money for icecream:- "))

# if icecream_amount == 10:
#     print("i will buy a Magnum")

# elif icecream_amount == 20:
#     print("i will buy a cornetto")

# elif icecream_amount == 30:
#     print("i will buy a cornetto")

# else:
#     print("i will buy a double Magnum")

# number1 = 0.0
# number2 = 0

# if number1 > number2:
#     print(f"{number1} is greater then {number2}")
# elif number2 > number1:
#     print(f"{number2} is greater then {number1}")
# else:
#     print(f"{number1} and {number2} are same")


# even or odd

# givenNumber = int(input("Number"))

# if givenNumber%2 == 0:
#     print('Even')
# else:
#     print('Odd')

# valid voter

# name_of_voter = input("tell me your name")
# age_of_voter = int(input("tell me your age"))

# if (age_of_voter >= 18):
#     print(f"{name_of_voter} are a valid voter")
# else:
#     print(f"{name_of_voter} your age is {age_of_voter} you are able for a vote after {18 - age_of_voter} years")


# leap year 
# year = int(input("tell me your birth year"))

# if year % 100 == 0 and year% 400 == 0:
#     print("leap year")
# elif year% 100 !=0 and year% 4 ==0:
#     print("leap year")
# else:
#     print("not a leap year")

# temprature

# temp = int(input("enter temprature"))

# if temp <= 0:
#     print("freezing cold")
# elif temp >= 0 and temp < 10:
#     print("very cold")
# elif temp >= 10 and temp < 20:
#     print("cold")
# elif temp >= 20 and temp < 30:
#     print("pleasant")
# elif temp >= 30 and temp < 40:
#     print("hot")
# elif temp > 40:
#     print("very hot")


# for loop

# rng = range(15,2,-1)

# for i in rng:
#     print(f"hello world no {i}")

# for i in range(31):
#     print(f"hello {i}")


# for i in range(19,10,-1):
#     print(i)

# for i in range(-5,-16,-1):
#     print(i)

# for i in range(1,11):
#     print(f"2 x {i} = {2 * i}")

# for i in range(10,101,10):
#     print(i)

# table = int(input("what number of table you want"))

# for l in range(table,table*10+1,table):
#     print(l)