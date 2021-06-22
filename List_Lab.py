#****************
# List
#***************

List = Define a group of values inside square brackets. 
# Its Haterogeneous 
# List is mutable. You can add/delete/modify the list values or objects.

lst = [1,2,3] # lst = list
lst[0]='Nescafe' # lst = ['Nescafe',2,3]
lst = [1,2,'Apple'] # list is a Hetrogeneous

tray = ['Nescafe','Brue','Taj'] # list
tray[0] # gives 'Nescafe' -> List uses the index to get the values.
# LetToRight side = indexing start from 0 to n-1
# RighToLeft side = indexing start from -1 to -n
# Lefthand side no = Before : element = is Inclusive
# Righthand side no = After : element = is Exclusive = index-1 elements
 
ltray = [1,2,3,4,5,6]
ltray[0] # gives first element from LetToRight of the ltray = 1
ltray[-1] # gives first element from RighToLeft of the ltray  = 6
ltray[-2] # gives 5

#******Slicing & Dicing ***

llist = [1,2,3,4,5,6,7,8,9,10]
llist[5:] # [5:] = LetToRight index 5 to End = 6th element to End = gives [6,7,8,9,10]
llist[:5] # [:5] = LeftToRight from start to till index 5 => index 5 = 6th element = Right hand side elemnt is exclusive => 0th element to 5th element = gives [1,2,3,4,5]

llist[2:9] # [2:9]=[start from 2 : Till 9-1 index] = gives [3,4,5,6,7,8,9]

llist[::3] # [::3] -> gives all 3rd elements in the row 
# gives [1,4,7,10] = 0th element, 3rd element, 6th element, 9th element = otherwords it returns the multiples of 3.

llist[3:-2] # [3:-2] = LeftToRight start from 3 To RighToLeft till -2(till second element from Right).
# For -ve index positions use the same value. It is inclusive. 
# gives [4,5,6,7,8]

#*********List Iteratoin - For loop*********

for coffee in tray:
pass # If you dont give pass, it will throw an error. Bcs tray is not defined yet.
# pass = reserved keyword = is do nothing

tray = ['Nescafe','Brue','Sunrise'] 
for coffee in tray:
print(coffee)       # returns all the values in the tray. 'Nescafe','Brue','Sunrise'

for coffee in reversed(tray):
print(coffee)       # It reversed the order of objects, returns 'Sunrise','Brue','Nescafe'

#*****Reverse Lists
names = ['Nescafe','Brue','Sunrise','Taj'] # list
names.reverse() # reverse the tray = gives ['Taj','Sunrise','Brue','Nescafe']

names_reversed = list(reversed(names))
names_reversed # reverse the tray = gives ['Nescafe','Brue','Sunrise','Taj'] 

names_reversed1 = names_reversed[::-1] # multiple with -1
names_reversed1 # gives ['Taj','Sunrise','Brue','Nescafe']

lst=[2,4,6,7,8]
8 in lst # gives true/false values = true
tray = ['Nescafe','Brue','Sunrise'] 
'Nescafe' in tray # gives true
'Nescafe' not in tray # gives false

Nescafe[::-1] # gives reverse of Nescafe = efacseN

#******Unpacking******

tray = ['Gift1','Nescafe','Brue','Sunrise','Gift5']
a, *_, b = tray # unpacking 
# a gives 'Gift1'
# b gives 'Gift5'
# _ gives ['Nescafe','Brue','Sunrise'] -> _ act as default variable. Can use any variable name.

a, *remaining, b = tray
# a gives 'Gift1'
# b gives 'Gift5'
# remaining gives ['Nescafe','Brue','Sunrise']

*c, d, e = tray
# d gives 'Sunrise'
# e gives 'Gift5'
# c gives ['Gift1','Nescafe','Brue']

























