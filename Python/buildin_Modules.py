#module is same as code library
#a python file has set of functions which we use in application
#import for reusablity
#to know build in modules

import math #import math module
import random#import random module
import time#import time module to get timespan
import os#import os module
#print(help("modules"))
#Math, random,os, time

#Math
print("get Pi value from math",math.pi)
print("get e value from math",math.e)
print("Print factorial of number using math",math.factorial(5))
print("print complete value",math.ceil(5.3))#6
print("print complete value",math.floor(5.3))#5
print("get squar root of number",math.sqrt(49))#7

#random
a=random.randint(1,100)#generate random number btwn given range
print("random number",a)
b=[1,2,3,4,5]
#it will shuffle iterable list,set,string,etc it will do for permanant
random.shuffle(b)
print("print shuffled list",b)#order get changes

#time
print("seconds passed till date from 1st jan 1970",time.time())
print("Print Current time",time.ctime())
print(time.time())
time.sleep(1)#delay btwn execution
print(time.time())

#OS module
print("get current working directory",os.getcwd())
print("list of all files in current directory",os.listdir())