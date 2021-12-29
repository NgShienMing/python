"""Python basics"""
#Variables
str = 'Ng Shien Ming' #str
int = 9278 #int
float = 93.63 #float
complex_num = 2+3j #complex
list = ['Ng', 'Shien', 'Ming'] #list/array
tuple = ('Ng', 'Shien', 'Ming') #tuple
dict = {'name': 'Ming', 'age': 19} #dict/object
set = {'Ng', 'Shien', 'Ming'} #set
frozenSet = frozenset({'Ng', 'Shien', 'Ming'}) #frozenset
boolean = True #bool
byte = b'Ming' #bytes
byteArr = bytearray(5) #bytearray
memView = memoryview(bytes(5)) #memoryview

#Loops
#Print items in list
for i in list:
    print(i)

#Print items in tuple
for i in tuple:
    print(i)

#Print items in set
for i in set:
    print(i)

#Loop through dictionary
for i in dict:
    print(i)           #Print keys in dict
    print(dict[i])     #Print values in dict
    print(i, dict[i])  #Print keys and values in dict

#Print keys in dict using dict.keys() method
for j in dict.keys():
    print(j)

#Print values in dict using dict.values() method
for j in dict.values():
    print(j)

#Print keys and values together using dict.items() method
for x, y in dict.items():
    print(x, y)
