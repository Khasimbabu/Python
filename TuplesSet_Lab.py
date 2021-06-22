#****************
# Tuples & Sets
#***************

lst = [1,2,3] # lst = list
lst[0]='Nescafe' # lst = ['Nescafe',2,3]
lst = [1,2,'Apple'] # list is a Hetrogeneous
# List is mutable. You can add/delete/modify the list values or objects.

t = (1,2,3) # t = tuple
#Tuple is immutable.Its an immutable list. You can't change the values or objects.
len(t) # it tells how many object in tuple t.

# Hetrogeneous = You can have textual & Numerical data
# Homogeneous = Same type of data. Either the data is textual or Numeric. It should be in 1form.

t = ('coffee',2) # tuple is a Hetrogeneous
t[0] # which gives 'coffee', You can acess the objects inside the tuple.
 
type(t) # gives tuple object

t = 4,5,6 # gives a tuple(4,5,6) output.python wil create an immutable tray, if the data has mutiple values and they dont give brackets. If it is a single value it will be consider as either integer or string.

t = (['a','b']) # gives ('a','b') -> Tuple converts a list into an immutable tuple.

t = ('Nescafe') # gives 'Nescafe -> Its a str type. Bcs 1 value will not be consider as tuple eventhough you put it in brackets.
t = ('Nescafe',) # gives ('Nescafe',) -> Its a tuple bcs of ,


#*************
Sets
#*******
# Set - It is a tray & remove duplicates from a list/string
# Intersection/Join/Difference

tray1 = ['Nescafe','Nescafe','Taj','Brook Bond'] # list object
tray2 = set(['Nescafe','Nescafe','Taj','Brook Bond']) # converting list object into a Set
# gives {'Brook Bond','Nescafe','Taj'}

tray2 = set(tray1) # gives {'Brook Bond','Nescafe','Taj'}

s1 = set('avinash') # gives {'a','h','i','n','s','v'} -> removed the duplicate 'a' from string 




















