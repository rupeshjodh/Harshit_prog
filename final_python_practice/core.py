# from itertools import count
# import re
# count = 0
# pattern = re.compile('ab')
# matcher = pattern.finditer('abaabaabaa')
# for match in matcher:
#     count+=1
#     print(match.start(),"............",match.end(),".............",match.group())
# print("The number of occurances:",count)

# =================================================================================

# import re
# matcher = re.finditer(".","a7b k@9z")
# for match in matcher:
#     print(match.start(),"....",match.group())

# =================================================================================
# import re
# matcher = re.finditer("a{2,4}","abaababa")
# for match in matcher:
#     print(match.start(),"...........",match.group())

# =================================================================================
# import re
# l = re.findall("[a-z]","a7b9c5kz")
# print(l)
# =================================================================================
# # sub()
# import re 
# s = re.sub("[a-z]","_","8a7b9c5kz") 
# print(s)

# subn()

# import re
# t = re.subn("[a-z]","#","8a7b9c5kz")
# print(t)
# print("The result strings :",t[0])
# print("The number of replacements:",t[1])

# # split()
# import re
# l = re.split(",","sunny,bunny,chinny,vinny,pinny")
# print(l)
# for t in l:
#     print(t)

# =================================================================================
# import re # for the 10 digit mobile number
# n = input("Enter number :")
# m = re.fullmatch("[0-9]\d{9}",n) 
# if m!=None:
#     print("Valid mobile number")
# else:
#     print("invalid mobile number")

# ===================================================================================

# import re
# f1 = open("input.txt","r")
# f2 = open("output.txt","w")
# for line in f1:
#     list = re.findall("[7-9]\d{9}",line)
#     for n in list:
#         f2.write(n+"\n")
# print("Extracted all mobile numbers into output.txt")
# f1.close()
# f2.close()

# ===================================================================================

# import re
# s = input("Enter Vehicle Registrastion Number :")
# m = re.fullmatch("MH[012][0-9][A-Z]{2}\d{4}",s)
# if m!=None:
#     print("Valid Vehicle Registration Number")
# else:
#     print("Invalid Vehicle Registration Number")

# ===================================================================================

# n = 0
# while n<=10:
#     print("Amol")
#     n+=1

# i = 0
# while True:
#     i+=1
#     print("Infinity")

# for i in range(4):
#     for j in range(4):
#         print("i=",i,"j=",j)


# for i in range(10):
    
#     if i == 7:
#         print("process id enough ..... please break !!!!")
#         break
    
#     print(i)

# cart = [10,20,600,70,80]
# for item in cart:
#     if item>500:
#         print("Place the order insurance must be required !!!!")
#         break
#     print(item)


# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# num = [10,20,30,40,0,50,60,70]
# for n in num:
#     if n == 0:
#         print("Hey how we can divide with zero....just skip it")
#         continue
#     print("100/{}={}".format(n,100/n))


# l = []
# print(type(l))
# print(id(l))

# l = eval(input("Enter the input :"))
# print(list(l))
# print(type(l))

# l = list(range(0,10,2))
# print(l)
# print(type(l))


# s = "Amol_Nagrale"
# l = list(s)
# print(l)

# s = "Learnig python is very easy"
# l = s.split()
# print(l)

# n = [10,20,30,40,50,60,70,80,90]
# print(n[2:7:2])
# print(n[0:5:3])
# print(n[5::-1])
# print(n[1:100])

# n = [10,20,30,40,50,60,70,80,90]
# n[3] = 100
# print(n)


# n = [10,20,30,40,50,60,70,80,90]
# i = 0
# while i<len(n):
#     print(n[i])
#     i+=1


# n = [10,20,30,40,50,60,70,80,90]
# i = 0
# while i<len(n):
#     print(n[i])
#     i+=1

# for i in n:
#     print(i)

# n = [10,20,30,40,50,60,70,80,90]
# for n1 in n:
#     if n1%2==0:
#         print(n1)

# l = ['A','B','C']
# x = len(l)
# for i in range(x):
#     print(l[i],'positive index',i,"number of iterations",i-x,"negative index")


# n = [10,20,30,340]
# l = len(n)
# print(l)

# n = [1,2,3,4,3,3,2,2,2]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))

# n = [1,2,3,4,3,3,2,2,2]
# print(n.index(1))
# print(n.index(2))
# print(n.index(3))
# print(n.index(4))
# print(n.index(5))

# l = []
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# l.append(50)
# print(l)

# l = []
# for i in range(101):
#     if i%10==0:
#         l.append(i)
# print(l)

# n = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# n.insert(1,888)
# n.insert(20,99)
# n.insert(-15,777)
# print(n)

# n3 = "pythonlanguage"
# n1 = ['A','B','C']
# n2 = ['D','E','F']
# n1.extend(n3)
# print(n1)

# n = [0, 10, 20, 30, 40,10,20,30,10,10,50, 60, 70, 80, 90, 100]
# print(n.pop(1))
# # print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n.pop())
# n.remove(100)
# print(n)

# n = [0, 10, 20, 30, 40,10,20,30,10,10,50, 60, 70, 80, 90, 100]
# # n.reverse()
# n.sort()
# n.sort(reverse=True)
# print(n)

# n = [0, 10, 20, 30, 40,10,20,30,10,10,50, 60, 70, 80, 90, 100]
# m = n[:]
# n[3]=101010
# m[3]=22222
# print(n)
# print(m)

# x = [0, 10, 20, 30, 40,10,20,30,1]
# y = x.copy()
# y[2] = 300
# print(x)
# print(y)

# x = [0, 10, 20, 30, 40,10,20,30,1]
# n = [0, 10, 20, 30, 40,10,20,30,10,10,50, 60, 70, 80, 90, 100]
# c = x+n
# c*=3
# print(c)


# x = [n*n for n in range(1,11)]
# x = [n*n for n in range(1,11) if n%2==0]
# x = {n:n*n for n in range(1,11)}
# print(x)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# s = "Learning python is very easy"
# n = len(s)
# i = 0
# print("forword direction")
# while i<n:
#     print(s[i],end="")
#     i+=1
# print("\n Backword direction")
# i = -1
# while i>-n:
#     print(s[i],end = "")
#     i = i-1

# s = "Learning python is very easy !!!!"
# print("forword direction")
# for i in s:
#     print(i,end="")
# print("\n backword direction")
# for i in s[::-1]:
#     print(i,end = "")

# s = "durga"
# print('d' in s)
# print('z' in s)

# s = "learning python is very easy "
# for i in s[::-1]:
#     print(i, end="")
# print("forword direction")
# for i in s[::]:
#     print(i, end="")

# # s = 'durgha'
# s = input("Enter the string :")
# r = reversed(s)
# output = "".join(r)
# print(output)

# s = "Learning python is very easy"
# l = s.split()
# l2 = []
# for i in l:
#     l2.append(i[::-1])
# output = " ".join(l2)
# print(output)

# s = "learning python is very easy"
# l1 = s.split()
# l2 = []
# for i in l1:
#     l2.append(i[::-1])
# output = " ".join(l2)
# print(output)

# s = "one two three four five six"
# l1 = s.split()
# i = 0
# l2 = []
# while i<len(l1):
#     if i%2==0:
#         l2.append(l1[i])
#     else:
#         l2.append(l1[i][::-1])
#     i+=1
# print(l2)
# output = " ".join(l1)
# print(output) 

# s = "Durga software solution"
# even_list = []
# odd_list = []
# for i in len(s):
#     if i%2==0:
#         even_list.append(i)        
#     else:
#         odd_list.append(i)

# print(even_list, end="")

# s = "durgasoft"
# for i in range(len(s)):
    
#     if i%2 == 0:        
#         print("The even number of charecters is ",s[i])
#     else: 
#         print("The odd number of charecters on given string is",s[i])


# for i in range(len(s)):
#     if i%2 ==0:
#         print("Even number",s[i])
#     else:
#         print("odd number",s[i])


# s = "A1D2FT3GHB489"
# # s = input("Enter only alphanumeric string ti sort :")
# Alphabets = [] 
# Digits = [] 
 
# for ch in s: 
#     if ch.isalpha():
#         Alphabets.append(ch) 
#     else:
#         Digits.append(ch) 
# output = ''.join(sorted(Alphabets)+sorted(Digits)) 
# print(output)

# for ch in s:
#     if ch.isalpha():
#         Alphabets.append(ch)
#     elif ch.isdigit():
#         Digits.append(ch)
# output = "".join(sorted(Alphabets)+sorted(Digits))
# print(output)


s ="A4B3C2"
# s = input("Enter the required sequence :")
output = '' 
# for ch in s:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)  
#         output = output + x*d
# print(output)

# for ch in s:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)
#         output = output +x*d
# print(output)

# s = 'a4m4o4l4'
# output = ''
# for ch in s:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)
#         output = output+ x*d
# final_output = "".join(output)
# print(final_output)

#input = a4k3b2 output = aeknbd

# s = input("Enter the required string : ")
# s = 'a4k3b2'
# output = ''   
# for ch in s:   
#     if ch.isalpha(): 
#         output = output+ ch 
#         x = ch     
#     else:
#         d = int(ch)   
#         newc = chr(ord(x)+d)  
#         output = output+newc
# print(output)


# def wish(name):
#     print("Hello",name,"Good morning")
#     """This is the good morning function"""

# wish("Amol")
# print(wish.__doc__)


# def squareit(value):
#     """This is the square function"""
#     return value*value

# print(squareit(5))
# print(squareit(6))
# print(squareit.__doc__)


# def decor(func):
#     def inner(name):
#         print("This is inner decor function")
#         func(name)
#     return inner

# def decor1(func):
#     def inner(name):
#         print("This is the inner1 decor function")
#         func(name)
#     return inner

# @decor1
# @decor

# def wish(name):
#     print(name,"This is the main function")

# wish("Amol")

# def mygen():
#     yield'A'
#     yield'B'
#     yield'C'
#     yield'D'

# g = mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen(n):
#     for i in range(10):
#         yield i

# g = gen(5)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# i = (x for x in range(1,101) if x%10==0)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# fabonacci series
# def fab(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else: return fab(n-2)+fab(n-1)

# for i in range(1,11):
#     print(fab(i))

# factorial

# def factorialit(n):
#     if n ==0:
#         result =1
#     else:
#         result=n*factorialit(n-1)
#     return result

# print(factorialit(4))


# def firstn(num):
#     n = 1
#     while n<=num:
#         yield n
#         n = n+1
# values=firstn(5)
# for x in values:
#     print(x)

# h = "harry"
# # for i in h:
# #     print(i)

# itr = iter(h)
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())

# i = [x*x for x in range(21000000000000000000000)]
# print(i)

# i = (x*x for x in range(21000000000000000000000))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import csv
# with open("abc.xl","w",newline='') as f:
#     w = csv.writer(f)
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n = int(input("Enter the number of employee:"))
#     for i in range(n):
#         eno =   input("Enter Employee Numbers :")
#         ename = input("Enter Employee Name :")
#         esal = input("Enter Employee Salary :")
#         eaddr = input("Enter Employee Address :")
#         w.writerow([eno,ename,esal,eaddr])
# print("total Employee data written to csv file successfully !!!")



# def decorator(any_function):

#     def inner_func(a, b):
#         if a>b:
#             any_function(a,b)
#         else:
#             any_function(b, a)
#     return inner_func

# @decorator
# def divide(a,b):
#     print(a//b)
# divide(100,50)
# divide(50,100)

# from functools import wraps
# def decorator(any_func):
#     @wraps(any_func)
#     def inner_func(a, b):
#         if a>b :
#             any_func(a,b)
#         else:
#             any_func(b,a)
#         return any_func(a,b)
#     return inner_func

# @decorator       
# def divide(a,b):
#     '''This is the division operation'''
#     print(a//b)

# divide(50,100)
# print(divide.__doc__)

# def reverse(s):
# 	if len(s) == 0:
# 		return s
# 	else:
# 		return reverse(s[1:]) + s[0]

# s = "Geeksforgeeks"

# print ("The original string is : ",end="")
# print (s)

# print ("The reversed string(using recursion) is : ",end="")
# print (reverse(s))


# s = 'python is easy language'
# s1 = "".join(reversed(s))
# print(s1)


from abc import ABC, abstractmethod
class Database(ABC):
    
    @abstractmethod
    def connect():
        pass
    
    @abstractmethod
    def disconnect():
        pass
        
class Mysql(Database):
    def connect():
        print("This is for mysql connect database")
        
    # def disconnect():
    #     print("This is disconnect database")
        
class MongoDB(Database):
    # def connect():
    #     print("This is for connect database")
        
    def disconnect():
        print("This is disconnect mdb database")
        
m = Mysql
m.connect()
m.disconnect()

m1 = MongoDB
m1.connect()
m1.disconnect()


