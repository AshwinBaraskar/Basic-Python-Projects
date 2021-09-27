'''extend'''
# list1=[10, 20, 30, "A"]
# list2=[40, 50, 60, "B"]
#
# val=list1.extend(list2)
#
# print(list1)

# from keyword import kwlist
# print(kwlist)


'''counting the list'''
# ele=['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# l=len(ele)
# print(l)
# a=0
#
# for cnt in ele:
#     print(cnt)
#     a += 1
# print(a)


'''type of the data'''
# import sys
# list=[10,20,30, 40, 60, 90, 10, 30, 20, 20, "A"]
# print("initial list:", list)
#
# val = [10, 20, 30, 40, "A", "B", True, "False", None]
# val = 103387378284732732472384
# print(val, type(val),sys.getsizeof(val))
#


'''sorted and sort
The primary difference between the list sort() function and the sorted() function is that the sort() function 
will modify the list it is called on. The sorted() function will create a new list containing a sorted 
version of the list it is given.'''
# list=[4, 3, 2, 6, 1, 5]
# L=sorted(list)
# print(L)
# print(sorted(L))
# print(sorted(L, reverse=True))
# print()
#
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
#
# print()

# L = ['aaaa', 'bbb', 'cc', 'd']
# print(sorted(L))
# print()
# print(sorted(L, key=len))

# list=[(4,5,1),(1,3,2),(5,4,2),(3,4,5)]
# list.sort()
# print(list)


'''LIST of dict--> sorted'''
# student = [{'name': 'john', 'score': 98}, {'name': 'mike', 'score': 94}, {'name': 'jennifer', 'score': 99}]
# l = sorted(student, key=lambda x: x['score'])
# # l = sorted(student, key=lambda x: x['name'])
# print(l)


# def sortSecond(val):
#     return val[1]
# list1 = [(1, 2), (3, 3), (1, 1)]
# list1.sort(key=sortSecond)
# print(list1)
#
#
# list=eval(input("Enter the list: "))
# print(list)


'''pop--> To remove and return last element of the list
if the list is empty then we get a Error'''
# list = [10, 20, 30, 20, 50, 60, "AA", "3283", "AA", "11", "10", 10]


# print(list.count(10))
# print(list.index(20))
# print(list[1:11:3])     #start index : end index : steps
#
# print("Original List: ", list)
# print(list.pop(), list)
# print(list.pop(), list)
# print(list.pop(), list)
# print(list.pop(), list)
# print(list.pop(1), list) #remove index wise

'''remove()--> To remove the specified element form the list and if element is present multiple times then first item will 
be removed
if specified item is not present then then we get ValueError'''
# n =[20, 10, 40, 20, 30, 10]
# n.remove(10)
# print(n)
# n.remove(50)
# print(50) #ValueError

#
# list.reverse()
# print(list)

# list.sort()
# print(list)   #homogeneous elements if not then get a TypeError

# print(10 in list)  #Membership operator
# print("AA" in list)
# print("AA " in list)

# list.clear() #to remove all the element
# print(list)

# for items in list:
#     print(items)
#

'''------------------------------------'''

# list="My name is Ashwin Manohar Baraskar"
# items=list.split()
# print(items) # ['My', 'name', 'is', 'Ashwin', 'Manohar', 'Baraskar']


list="My name is Ashwin Manohar Baraskar".split()
#
# l=[[w.upper(), len(w)]  for w in list]        ######## list=[condition and expression    loop or cond]
# print(l)


# list1=[10, 20, 30, 40,90, 101,50, 60]
# print(max(list1))
# print(min(list1))

'''The enumerate() method adds counter to an iterable and returns it (the enumerate object).'''
# grocery=['bread', 'milk', 'butter']
#
# print(dict(enumerate(grocery)))   #<enumerate object at 0x02BA4788>
# obj=dict(enumerate(grocery, 10))
# print(obj)
#
# a=enumerate(list)
# for items in a:
#     print(items)

# print()
# for key, val in enumerate(list):
#     print(key, val)
# print()
#
# for key, val in enumerate(list, 10):
#     print(key, val)
# print()
#


'''Membership operator and while'''
# while True:
#     list = ["y", "yes"]
#     ch = input("do you want to continue: ")
#     if ch.lower() not in list:            #run upto it gets false
#         break


'''How to generate a list: 1'''
# list = []
# for i in range(11):
#     list.append(i)
#     print(i)
# print(list)

'''How to generate a list: 2'''
# def list_gen(num):
#     for i in range(1, num):
#         yield i
#
# values = list_gen(10)
# l1 = list(values)
# print(l1)


'''ASCII Code
A-Z --> 65 to 90
a-z --> 97 to 122
0-9 --> 48 to 57
'''

# import random
# st = " "
# for j in range(6):
#     char = random.randint(65, 90)
#     st += chr(char)
# print(st)
#
# st1 = " "
# for j in range(6):
#     char = random.randint(65, 90)
#     st1 += chr(char)
# print(st1)
# ch = [st, st1]
#
# dic = []
# for i in range(2):
#     person = {
#         "id" : i+1,
#         "name": ch[i]
#     }
#     dic.append(person)
# print(dic)


# lang = [['Python', 'java', 'ML'], ['Angular', 'java', 'Django'], ['AWS', 'Flask', 'DS']]
#
# for i in lang:
#     print(i)
#     for lan in i.languages:
#         print(lan)


'''Adding to list elements'''
# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 3, 4, 5]
# list = []
# for i in range(len(list1)):
#     list.append(list1[i]+list2[i])
# print(list)


# import random
# deck=list(range(1,53))
# print(deck)
# random.shuffle(deck)
# print(deck)