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

# print(12 < 15 and 12 < 14 or 12 < 14 )

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


# aa = "muhammad"

# for i in range(8):
#     print(aa[i])

# s = "abcdefghijklmnopqrstuvwxyz"

# for i in range(len(s)):
#     print(s[i])

# s = "abcdefghijklmnopqrstuvwxyz"
# for i in s:
#     print(i)

# for i in range(22):
#     if i == 21:
#         print("break executed")
#         break
#     print(i)
# else:
#     print("break not executed")

# n = int(input("tell me a number"))

# for i in range(n):
#     print(f"hello world {n}")

# for i in range(1,n+1):
#     print(i)

# for i in range(n,0,-1):
#     print(i)

# for i in range(n,n*10+1,n):
#     print(i)

# sums = 1
# for i in range(1,n+1):
#     sums += i

# print(sums)

# for i in range(1,n+1):
#     sums = sums * i

# print(sums)


# n = int(input("tell me a number"))

# even = 0
# odd = 0

# for i in range(1,n+1):
#    if i%2 == 0:
#       even = even + i
#    else:
#       odd = odd + i

# print(f'sum of the even and odd number are {even}, {odd}')

# n = int(input("tell me a number"))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

# n = int(input("tell me a number"))
# perfect = 0
# for i in range(1,n):
#     if n%i == 0:
#         perfect = perfect + i

# if perfect == n:
#     print("prefect number")
# else:
#     print("not a perfect number")

# n = int(input("tell me a number"))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# print(count)
# if count == 2:
#     print("prime num")
# else:
#     print("not a prime num")

# s = input("whats your name")
# concat = ""

# for i in range(len(s)-1,-1,-1):
#     concat = concat + s[i]

# if (concat == s):
#     print("your name is pallindrome")
# else:
#     print("your name is not a pallindrome")

# mixStr = "!@^&*(()hhaxhajbx1sq7739221"

# digit = 0
# characters = 0
# special_characters = 0

# for i in mixStr:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         characters += 1
#     else:
#         special_characters += 1

# print(digit,characters,special_characters)

# w = 1

# while w <= 5:
#     print(f"hello world {w}")
#     w = w + 1

# print(2//10)

# wh = int(input('num'))

# while wh > 0:
#     print(wh % 10)
#     wh = wh // 10


# wh = int(input('num'))
# rev =0

# while wh > 0:
#     rev = rev * 10 + wh % 10
#     wh = wh // 10
# print(rev)


# wh = int(input('num'))
# rev = 0
# wh_copy = wh

# while wh > 0:
#     rev = rev * 10 + wh % 10
#     wh = wh // 10

# if wh_copy == rev:
#     print('pallindromic num')
# else:
#     print('non pallindromic num')


# functions 

# def hello():
#     print("hello")

# hello()

# parameter and arrgument in functions

# the thing you want to accept is parameter
# the thing you provide to parameter is arrgument

# def sum(a,b):
#     print(f"the sum of {a} and {b} = {a + b}")

# sum(12,12)


# pallindrome function


# def pallindrome (str):

#     reverse_string = ""

#     for i in range(len(str)-1,-1,-1):
#         reverse_string = reverse_string + str[i]
    
#     if (reverse_string == str):
#         print(f"pallindrome")
#     else:
#         print(f"not pallindrome")

# # pallindrome("haram")

# def return_func():
#     return "return val"

# print(return_func())


# list -------------------

# a = [11,12,13,14,15,16,17,18,19,20]

# print(len(a))
# a[0] = 10
# print(a[0:5:1])

# 1st way to run loop using index

# for i in range(len(a)):
#     print(i) #index
#     print(a[i]) #values

# 2nd way directly on values

# for i in a:
#     print(i)


# a = [11,12,13,14,15,16,17,18,19,20,20]

# a.append("haram") #add value in last of the list (value)
# a.insert(0,10) #add value ("index","value")
# a.extend([21,22,23,24,25]) #add multiple values in last of the list ([value,value,value])
# print(a)

# names = ["haram","harris","hasnain","kivi","wahid","saleem"]

# names.remove("haram") #remove the first occurrneces of haram
# has = names.pop(2) # remove the store the element
# print(has)

# index = names.index("haram")
# print(index)

# print(names)

# count = a.count(20)
# print(count)

# num = [1,5,6,9,2,4,3,10]

# num.sort()
# print(num)

# list questions 

# negative and positive values

# pos_neg = [-45,12,3,4,-5,-6,6,8,-8,-100]

# print("positive values")
# for i in pos_neg:
#     if i >= 0:
#         print(i)

# print("negative values")
# for i in pos_neg:
#     if i < 0:
#         print(i)


# mean = [1,2,3,4]

# mean_total = 0

# for i in range(len(mean)):
#     mean_total = mean_total + mean[i]

# print(mean_total/len(mean))

# fg_number = [100,200,500,300,50,60,1000,20,10,40]

# l_number = fg_number[0]
# sl_number = fg_number[0]
# index = 0

# for i in range(len(fg_number)):
#     if  fg_number[i] > l_number:
#         l_number = fg_number[i]

#         index = i

# print(l_number,index)


# f2l_number = [10,12,1,2,95,3,4,5,6,34,0]
# larget_number = f2l_number[0]
# second_larget_number = f2l_number[0]

# for i in f2l_number:
#     if i > larget_number:
#         second_larget_number = larget_number
#         larget_number = i
#     elif i > second_larget_number:
#         second_larget_number = i

# print(larget_number)
# print(second_larget_number)

# sorted = [1,2,3,4,5,6,7,8,4,9,10]
 
# for i in range(len(sorted)-1):
#     if(sorted[i] <= sorted[i + 1]):
#         continue
#     else:
#         print('not sorted')
#         break
# else:
#     print('sorted')

# tuple 

tup = (1,2,3,4,5,6,6,6,print("tuple"),"haram",True)

# print(type(tup))

# print(tup[4])

# for i in tup:
#     print(i)

# tuple have two methods one for index findin and one is for count

# index = tup.count(6)
# print(index)

# tuple unpacking 

# t1,t2,t3,t4,t5,t6 = (1,2,3,4,5,6)

# print(t3)

# print(type(t3))


# sets

# s = {1,4,7,3,}
# ss = {2,3,4,5,6,7,8}

# # union = s.union(ss)
# intersec = ss.symmetric_difference(s)

# print(intersec)

# sim = 100
# sim2 = hash(sim)
# print(sim2)

# dictinory

# d = { 
#     "name":"haram",
#     "age":"21",
#     "location":"Jamshed road"
#     }

# print(d["name"])
# print(d["age"])
# print(d["location"])



# d.update({"university":"MAJU"})

# # we can perform "CRUD" opertion using dictinory


# d["name"] = "haris" #updating
# d["Subject"] = "AI" #creating
# del d["Subject"] #delete

# print(d)

# treversing or iteration in dictionary

# d = { 
#     "name":"haram",
#     "age":"21",
#     "location":"Jamshed road"
#     }

# for i in d:
#     print(d[i])

# help(dict)


# D_C1 = [1,2,3,4,5,6]

# D_C2 = D_C1

# D_C2[0] = "haram"

# print(D_C1)

# m_dic1 = {1:100,2:200,3:300,4:400}
# m_dic2 = {4:500,5:500,6:600,7:700}

# for i in m_dic2:
#     m_dic1[i] = m_dic2[i]

# print(m_dic1)

# m_dic1 = {1:100,2:200,3:300,4:400}
# m_dic2 = {4:500,5:500,6:600,7:700}

# sum = 0

# for i in m_dic1:
#     sum += m_dic1[i]

# print(sum)

# f_elem = [1,1,1,1,3,3,3,2,2,2,4,4,4,56,7,8,9,0,0,0,0,0,0,0,0,0]
# d = {}

# for i in f_elem:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

m_dic1 = {1:100,2:200,3:300,4:400}
m_dic2 = {4:500,5:500,6:600,7:700}

for i in m_dic2:
    if i in m_dic1:
        m_dic1[i] += m_dic2[i]
    else:
        m_dic1[i] = m_dic2[i]

print(m_dic1)