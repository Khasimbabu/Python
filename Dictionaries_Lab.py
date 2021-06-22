#****************
# Dictionaries
#***************

# Dictionary is a tray which has keys & values = {key : value}
# Dictionary is a mutable. You can modify the values inside a Dictionary.

traypens = {'cap1':'Reynolds','cap2':'Parker'} # traypens = Dictionary 
# keyes = 'cap1','cap2'
# values = 'Reynolds','Parker'

tuple1 = tuple({'cap1':'Reynolds','cap2':'Parker'}) # taking dictionary into a tuple & converting the dictionary into a tuple. 
# gives ('cap1','cap2') -> Tuple only taking keys from dictionary and return.

tray = ['Nescafe','Brue','Taj'] # list
tray[0] # gives 'Nescafe' -> List uses the index to get the values.

dtray = {'Coffee':'Nescafe','Filter':'Brue','Instant':'Sunrise'} # dictionary
dtray['Coffee'] # gives 'Nescafe' -> Dictionary uses the Keys to get the values.
# dictionary = {key:value}
# keys can't be duplicated & values can be duplicated 

dtray['Filter'] = 'Brue Bond'
dtray # gives {'Coffee':'Nescafe','Filter':'Brue Bond','Instant':'Sunrise'}

dtray['continental'] = 'Latte'
dtray # gives {'Coffee':'Nescafe','Filter':'Brue Bond','Instant':'Sunrise', 'continental':'Latte'}
# If the key is not present then dictionary adding the key & value
# If the key is present then dictionary modify the value.

dtray['expresso'] = 'Latte'
dtray # gives {'Coffee':'Nescafe','Filter':'Brue Bond','Instant':'Sunrise', 'continental':'Latte', 'expresso':'Latte'}

# You can't have keys duplicated. But you can have duplicate values. Keys are unique.

dtray.keys() # gives all the keys in the dictionary.
# dict_keys(['Coffee','Filter','Instant','continental','expresso'])
dtray.values() # gives all the values in the dictionary.
# dict_values(['Nescafe','Brue Bond','Sunrise','Latte','Latte'])

dict = {'c': 97, 'a': 96, 'b': 98}
for _ in sorted(dict):
    print (dict[_]) # gives 96 98 97


































