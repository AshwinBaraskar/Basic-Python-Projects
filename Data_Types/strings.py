'''ASCII Code
A-Z --> 65 to 90
a-z --> 97 to 122
0-9 --> 48 to 57
'''

'''What is String?
Any sequence of characters within either single quotes or double quotes is considered as a String.

start pt : upto that pt : steps
         :
string length'''
# string = "Ashwin Baraskar"
# print(string[0:3])    #0 to n-1 -->print
#
# print(string[0:6:3])   #0 to 6 --> steps of 3
# print(string[0::2])    # start pt : not mention : steps
# print(string[::])  #asitis
# print(string[:])    #asitis
# print(string[::-1])   #reverse
# print(string[::-2])    # :: steps
# print(string[::2])
# print(string[:2:])
# print(string[:6:])      # by default zero : upto pt : 0
# print(string[2::])


'''to print quote: \' '''
# s='This is \' single quote symbol'
# s1='The \"Python Notes\" by \'durga\' is very helpful'
# print(s1)

# str="Ashwin"
# print(len(str))


'''split(): it provides the list of words'''
# message=input("Enter the text: ")
# words=message.split()
# print(words)


# lines = '''12 34
#             56
#             789'''
# print("working of split function: ", lines.split())
# char_count = 0
#
# for line in lines:
#     character = line.split()
#     char_count = char_count + len(character)
# print("character in the given text: ", char_count)
#
# word=0
# for line in lines.split():
#     word = word + 1
# print('Total words: ', word)
#
#
# No_lines = lines.split('\n')
# print('No of lines: ', len(No_lines))


'''count()--> counts the number of times substring occurs in the given string and returns an integer '''
# string = "geeks for geeks"
# print(string.count("geeks"))
#
# print(string.count("geeks", 0, 5))
# print(string.count("geeks", 0, 15))

'''videos'''
# city=input("Enter your city Name:")
# scity=city.strip()
# # print(scity)      # give spaced string
# if scity=='Hyderabad':
#     print("Hello Hyderbadi..Adab")
# elif scity=='Chennai':      # give spaced string
#     print("Hello Madrasi...Vanakkam")
# elif scity=="Bangalore":
#     print("Hello Kannadiga...Shubhodaya")
# else:
#     print("your entered city is invalid")

'''1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
    2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
    3) isdigit(): Returns True if all characters are digits only( 0 to 9)
    4) islower(): Returns True if all characters are lower case alphabet symbols
    5) isupper(): Returns True if all characters are upper case aplhabet symbols
    6) istitle(): Returns True if string is in title case
    7) isspace(): Returns True if string contains only spaces'''
# print('Durga786'.isalnum()) #True
# print('durga786'.isalpha()) #False
# print('durga'.isalpha()) #True
# print('durga'.isdigit()) #False
# print('786786'.isdigit()) #True
# print('abc'.islower()) #True
# print('Abc'.islower()) #False
# print('abc123'.islower()) #True
# print('ABC'.isupper()) #True
# print('Learning python is Easy'.istitle()) #False
# print('Learning Python Is Easy'.istitle()) #True
# print(' '.isspace()) #True


'''first repeated character: '''
# def firstRepeatedChar(str):
#     h = {}  # Create empty hash
#     # Traverse each characters in string
#     # in lower case order
#     for ch in str:
#         # If character is already present
#         # in hash, return char
#         if ch in h:
#             return ch
#             # Add ch to hash
#         # else:
#         #     h[ch] = 0
#     return
# # Driver code
# name = input("Enter the string: ")
# print(firstRepeatedChar(name))

'''
to print most repeat character in the string
'''
# s = 'my name is mohan munna'
# count = 0
# for i in s:
#     for j in s:
#         if i == j:
#             print(i)
#

# '''Print the key who's value is maximum'''
# d = {'a': 1, 'c': 2, 'd': 5, 'e': 1, 'i': 1, 's': 2, 'o': 3}

# import collections
# str1 = 'my name is mohanmuna'
# d = collections.defaultdict(int)
#
# for c in str1:
#     d[c] += 1
# print(d)
#
# for c in sorted(d, key=d.get, reverse=True):
#     if d[c] > 1:
#         print(c, d[c])




# from collections import Counter
#
# sample_string = 'thequickbrownfoxjumpsoverthelazydog'
# cate = Counter(sample_string)
# for k, v in cate.items():
#     print(k, v)



