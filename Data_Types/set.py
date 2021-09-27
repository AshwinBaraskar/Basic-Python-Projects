'''diffence method'''
# set1={10, 20, 30, "A"}
# set2={10, 30, 40, "B", 50, 60}
# print("set1: ", set1)
# print("set2: ", set2)
#
# print("difference--set1:", set1.difference(set2))
# print("differnce--set2: ", set2.difference(set1))
#
# set1.difference_update(set2)
# print("differnce_update--set1: ", set1)
# #here we updated the first set and if we try to run both i.e. set2 then we get diff output
# returnval2 = set2.difference_update(set1)
# print("difference_update:--set2: ", set2)


# set = {10, 20, 30, 40, 50, 60, "AA", "3283", "AA", "11", "10", 10, 10} #can not contain duplicate items
# print(set)


# set = {10, 20, 30, 40, 50} #sequence does not maintain
# print(set)


'''add--> adds one item to the set'''
# set = {10, 20, 30, 40}
# set.add(50)
# print(set)


'''update -->To add multiple items to the set or to make concat'''
# set = {10, 20, 30, 40, 50, 'A'}
# set.update('B')
# print(set)
# set1 = {60, 70, 80}
# set.update(set1)
# print(set, "\n")
# list = [1, 2, 3, 4]
# set.update(list)
# print(set)
#
# set1 = {1, 2, 3, 4, 5, 6, 7}
#
# set.update(set1)
# print(set)

'''frozenset Data type = It is exactly same as set except it is immutable'''

# s = {10, 20, 30, 40, 50}
# fs = frozenset(s)
# print(type(fs))
# print(fs)

'''pop --> It removes and return the random element from the set'''
# s1 = {10, 20, 30, 40, 50, 60, 70 , 80}
# print(s1.pop())
# print(s1)

'''remove()--> It removes the specified element from the set
element is not present --> get key error'''
# s1 = {10, 20, 30, 40, 50, 60, 70 , 80}
# s1.remove(10)
# # print(s1)
# # s1.remove(100)

'''discard()--> It removes the specified element form the set.
If ele is not present the we won't get any error'''
# s1 = {10, 20, 30, 40, 50, 60, 70 , 80}
# s1.discard(10)
# print(s1)
# s1.discard(100)
# print(s1)

