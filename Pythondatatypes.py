# Python int,float,string  datatypes
try:
    print("****************int/float operations************")
    a=5
    print (type(a) ,a )
    f=5.2
    print (type(f),f)
    c=a+f
    print(type(c),c)
    s ='sample'
    print(type(s),s)
    # TypeError: can only concatenate str (not "int") to str
    k=str+a
    print(type(k),k)
    print("****************************")
except Exception as e:
    print(e)
    print("****************************")

#python  list operations
# empty list
try :
    print("***********Python List Operations*****************")
    a = []
    print (a)

    # list of integers
    a = [1, 2, 3,7,8,9]
    print (a)
    #list element
    print(a[0],a[1])
    #negative index
    print(a[-1])
    #start index and end index
    print(a[2:5])
    print (a[:-3])
    print (a[3:])
    print (a[-3:])
    #length of the list
    print(len(a))
    a=[1,2,3]
    b=[4,5,6]
    print("list1:",a)
    print("list2:",a)
    #list concatenation
    print("list1+list2 :",a+b)
    # list with mixed datatypes
    mix_list = [1, "Hello", 3.4]
    print(mix_list)
    print(mix_list[0],mix_list[1])
    print(mix_list[1][0])
    print(mix_list[1][0:2])
    # list with nested lists
    nest_list=[1,[7,8,9],[10,200,20],300]
    print(nest_list[1])
    print(nest_list[1][2])
    print(len(nest_list))
    nest_list[2]=[50,60,70,90]
    print(nest_list)
    nest_list.remove(300)
    print(nest_list)
    del nest_list[0]
    print(nest_list)
    nest_list.append(300)
    print(nest_list)
    nest_list.pop()
    print(nest_list)
    nest_list.insert(1,23)
    print(nest_list)
except Exception as e:
    print(e)
#tuple operations
try:
    my_tuple = ()
    print(my_tuple)  # Output: ()
    # Tuple having integers
    my_tuple = (1, 2, 3)
    print(my_tuple)  # Output: (1, 2, 3)
    # tuple with mixed datatypes
    my_tuple = (1, "Hello", 3.4)
    print(my_tuple)  # Output: (1, "Hello", 3.4)
# nested tuple
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
    print(my_tuple)
    print(my_tuple[0])
    # cannot change the tuple value
    #my_tuple[0]='rat'
    a,b,c=my_tuple
    print(a,b,c)
    my_tuple=3, 4.6, "dog"
    print(my_tuple)
    my_tuple = ("hello")
    print(type(my_tuple))  # <class 'str'>
    # Creating a tuple having one element
    my_tuple = ("hello",)
    print(type(my_tuple))  # <class 'tuple'>
    # Parentheses is optional
    my_tuple = "hello",
    my_tuple = 3, 4.6, "dog"
    print(my_tuple[0])
    print(my_tuple[0:1])
    print(my_tuple[-1])
    print(type(my_tuple))  # <class 'tuple'>
    c=len(my_tuple)
    print(c)
    print(my_tuple.count("dog"))
    print(my_tuple.index("dog"))
    del my_tuple
    a=(1,2,3)
    b=(4,5,6)
    print(a+b)
except:
    print ('Error in tuple operations')
str1 = 'Hello'
str2 ='World!'
# using * for repeating
print('str1 * 3 =', str1 * 3)
print('str1 + str2 = ', str1 + str2)
del str1
str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
#character count
print('len(str) = ', len(str))
#TypeError: 'str' object doesn't support item deletion
#del str2[0]
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

#nge this value for a different output
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)
print(list(rev_str))
print(my_str)
# check if the string is equal to its reverse
#if list(my_str) == list(rev_str):
if my_str ==rev_str:
   print("It is palindrome")
else:
   print("It is not palindrome")

   numList = ['1', '2', '3', '4']
   seperator = ', '
   print(seperator.join(numList))

   numTuple = ('1', '2', '3', '4')
   print(seperator.join(numTuple))

   s1 = 'abc'
   s2 = '123'

 # Each character of s2 is concatenated to the front of s1"""
   print('s1.join(s2):', s1.join(s2))

# Each character of s1 is concatenated to the front of s2"""
   print('s2.join(s1):', s2.join(s1))
   #built in string functions
   s1='hellOworld'
   print(s1.capitalize())
   print(s1.casefold())
   print(s1.swapcase())
   print(s1.find('l',0,7))
   print(s1.replace('l','L',2))
   print(s1.replace('l', 'L', 1))
   print(s1.replace('l', 'L'))
   print(s1[0:5])
# dict operations
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print (my_dict)

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print (my_dict)
# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print (my_dict)
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print (my_dict)
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])
print(my_dict['age'])
# Output: 26
print(my_dict.get('age'))
print(my_dict.get('name'))
# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# remove a particular item
# Output: 16
print(squares.pop(4))
# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
#del squares[5]
# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares)

# set  operations
# set of integers
my_set = {1, 2, 3,2}
print(my_set)
my_set = set([1,2,3,2])
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
a={1,2,3,4,5}
b={4,5,6}
print("set 1 :",a)
print("set 2 :",b)
print ("set 1 union set 2 :", a | b)
print ("set 1 intersection set 2 :", a & b)
print ("set 1 difference set 2 :", a - b)
print ("set 2 difference set 1 :", a - b)
print(my_set)