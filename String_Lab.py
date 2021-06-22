#****************
# String
#***************

str='abcdefcdyzcd' 
print(str.split('cd',2)) # gives ['ab','ef','yzcd']

str='PYTHON\nString\nConcepts'
print (str.splitlines()) # gives ['PYTHON', 'String', 'Concepts']

print ('hi'.zfill(5)) # gives 000hi

fruit=['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit) # used to shuffle the objects in the list

l = [1, 2, 3]
tuple_a = ('Python',) * (l.__len__() - l[::-1][0]) # gives ()
print(l.__len__()) # gives length = 3
print(l[::-1]) # gives [3,2,1]

