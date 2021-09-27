'''popitem()It removes the arbitrary key-value pair from the dictionary and returns it as a tuple.
In versions before 3.7, the popitem() method removes a random item.'''

# car = {"brand": "Ford", "model": "Mustang", "year": 1964, "AA": 10, 1212: 12}
# print(car.popitem())
# print(car.popitem())
# print(car)


'''setdefault()'''
# values = {"a":100,"b":200,"c":300}
# ans = values.setdefault("c", 400) # No change because key is present
# print(values)
# print(ans)
# ans = values.setdefault("d", 400) # if key is absent then add
# print(values)
# print(ans)

'''How to combine to dictionary together
3 methods'''
# val1 = {1: 334, 2: 110, 3: 000}
# val2 = {4: 344, 5: 445, 6: 66}
# '''1'''
# val1.update(val2)
# print(val1)


'''2'''
# result = {**val1,**val2} #will return new
# print(result)


'''3'''

# val1 = {1: "A", 2: "B", 3: "C"}
# val2 = {4: "X", 5: "Y", 6: "Z"}
# for key, val in val2.items():   #to merge the two list
#     # print(key,":", val)
#     val1[key]=val
# print(val1)
#
# import sys
# d={}
# a=d*10000
# print(sys.getsizeof(a))
#

# dict = {1:100, 2:200, "A":112}
#


'''to give keys to index'''
# listOfVal = [5, 6, 7, 8, 9, 10, None, None] #array mutable dp seq index mulNone
# #listOfVal.reverse()
#
# dictVal = {}
# index = 0
# for index,item in enumerate(listOfVal):
#     print(item,index)
#     dictVal[item]=index   #assigning the value to the index
#     index+=1
# print(dictVal)
# print(index)
#
# dictOfVal = {1:22, 2:55, "A":"667", "B":78, None:889}
# print(dictOfVal['A'])  #just to access string character with string
'''-------------'''
# print('Dict--')
# for item in dictOfVal.keys():
#     print(item, dictOfVal[item])  #dictOfVal[item] used to get value
# print()
#
# print('dict values -- ')
# for item in dictOfVal.values():
#     print(item) #only values--
# print()
#
#
# print('dict pair')
# for pair in dictOfVal.items():
#     print(pair)
# print()
#
#
# print('dict pair')
# for key,val in dictOfVal.items():
#     print(key,val)

# dictOfVal.get(2343)       #value -- if we are not sure key present/absent -- !key=None
# dictOfVal[2343]           #2343 value -- present --agr --!key = error


# print(dictOfVal.get(3))
# print(dictOfVal[2])

# for key in dictOfVal.keys():
#     print(dictOfVal.get(key))  #dictOfVal[item] used to get value
# print()

'''How to create a dictionary'''
# d = {}
# name = int(input('Enter the Name:'))
# addr = input("Enter the addr: ")
# d[name] = addr
# print(d)


'''Print the key who's value is maximum'''
# d = {'a': 1, 'c': 2, 'd': 5, 'e': 1, 'i': 91, 's': 2, 'o': 3, 'z': 88}
#
# v = max(d.values())
# print(v)
# keys = list(d.keys())
# print(keys)
# vals = list(d.values())
# print(vals)
# print(keys[vals.index(v)])


# d = {'a': 1, 'c': 2, 'd': 5, 'e': 1, 'i': 1, 's': 2, 'o': 3, 'z': 88}
# l = []
# for v in d.values():
#     l.append(v)
# l.sort()
# key = l[-1]
# k=list(d.keys())
# val = list(d.values())
# print(k[val.index(key)])



'''How to add two dictionaries '''
# from collections import Counter
# dict1 = {'a': 10, 'b': 20, "c": 30, 'd': 40}
# dict2 = {'a': 10, 'b': 22, "c": 32, 'd': 40}
#
# d1 = Counter(dict1)
# d2 = Counter(dict2)
# print(d1)
# print(d2)
#
# print(d1+d2)



'''Is tuple,list can be key or not'''
# dict1 = {(10,20,30): 10, ('b','c'): 20, "c": 30, 'd': 40}
# print(dict1)

# dict1 = {[10,2,4,5]: 10, 'b': 20, "c": 30, 'd': 40}
# print(dict1)              # error

# dict1 = {(10,[10,20,30]): 10, 'b': 20, "c": 30, 'd': 40}
# print(dict1)