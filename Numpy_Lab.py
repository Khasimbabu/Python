#****** Numpy **********#
# Numpy is a package for Arrays and Matrices

import numpy as np

_list = [0,1,2,3,4]

_arr1d = np.array(_list)

# array can have numeric or textual data
# Most important thing about array is we can do airthematic operations

_arr1d + 2

print(_arr1d * 4)
print(_arr1d / 2)
print(_arr1d - 2)

#*****
np.zeros(5)
np.ones(5)

np.ones(5) * 2 
#For displaying all 2's in the array, bcs np.twos(5) not work. 
#It works for zero/one bcs these are binaries understand by computer
# Vectorised operation. Its a 1 dimentional array

np.zeros((2,2)) # Two dimentional array = Matrix
np.ones((2,2)) # Two dimentional array = Matrix

np.ones((2,2))*2 # Multiply 2 with all the elements of the Matrix

n.ones((2,3)) # 2rows and 3 columns

#***** Merging arrays
arr1 = np.matrix([1,2,3]) 
# When you give 1dimention to Matrix, it wil convert to 2 dimentional
arr2 = np.matrix([4,5,6])

print('Horizontal append:', np.hstack((arr1,arr2))) # hstack = horizontal stack
print('Horizontal append:', np.vstack((arr1,arr2))) # hstack = Arrange in Verticaly

#******

arr2d1 = np.array([[1,2],[3,4]])
print(arr2d1);

arr2d2 = np.array([[5,6],[7,8]])
print(arr2d2);

print('Horizontal append:', np.hstack((arr2d1,arr2d2))) # hstack = horizontal stack
print('Horizontal append:', np.vstack((arr2d1,arr2d2)))

#*******************************************

x = np.array(range(100)) # it print the numbers from 0 to 99.
x.ndim # gives no of axes/dimension = x is 1 dimension array

x.shape # It will gives rows and columns = 100 rows & 0 columns
x.size # gives how many objects/elements are there in an array
x.dtype # type of elements 

y = np.array([[1.0,2,3],[4,5,6],[7,8,9]])
y.ndim # its 2 dimentional

y.shape # 3 rows & 3 columns
y.size # gives size, its 9
y.dtype # float bcs one element in the array is decimal, so it treats all as decimal

np.full((5,5),53) # full = creates 5 rows,5 columns & all the values are 53

x = np.array([[1,2,3],[4,5,6]])

np.full((x.shape,53)) # Gives 2*3 matrix & all the values are 53

np.eye(5) # gives 5*5 matrix & diagnol elements are filled with 1 value & others are zeros

np.eye(5,3) # gives 5 rows and 3 columns & diagnol elements are filled with 1 value & others are zeros

x = np.array(range(90)) # gives 0 to 89 (90 is exlusive)
x = x.reshape((10,9)) # reshape the array values to 10 rows & 9 columns
x = x.reshape((3,3,10)) 
# (3,3,10) = (a,b,c)
# a = dimension, b= rows, c= columns
# each Bunch elements = b*c = 3 * 10 = 30
# each bunch has b rows * c columns
# 30 * 3 = 90 = Total elements = 3 bunches

x = np.array((range(90)).reshape(10,3,3)
# (10,3,3) = (a,b,c)
# 3 parameters = 3 dimentional 
# a = 10, b= rows, c= columns
# each Bunch elements = b*c = 3 * 3 = 9
# each bunch has b rows * c columns
# 9 * a = 90 = Total elements = 10 bunches

x.ravel # ravel = lowering the no of dimensions. Converts the multi dimension to 1 dimension. 3 dimension x converted to 1 dimension.

x = np.array((range(90)).reshape(10,3,3)
x.T # T = Transpose = convert 10 bunches to 3 bunches. 
T(10,3,3) = (3,3,10)
# From each bunch = concat all 1st row elements & arrange them in 1 row = r1,r2,r3...
# then concat all 2st row elements & arrange them in 2 row = r1,r2,r3...
# then concat all 3st row elements & arrange them in 3 row = r1,r2,r3...

x.T.shape # gives (3,3,10)

x = np.array(range(1,101)) # gives 1 to 100

x.sum() # sum = will sum all the values of x
x.min() # min = gives minimum value
x.max() # max = gives maximum value
x.mean() # mean = gives average value
x.std() # std = gives standard deviation
np.median(x) # median = gives median vars
np.mean(x) # similar to x.mean(), Arrays has built in all these function.
np.sqrt(x) # sqrt = return the sqrt of individual values

x = np.array(range(100)).reshape(10,10) # gives 0 to 99 elements & 10rows*10columns

#********* Slicing & Dicing *******
# Positions start from [0,0]

x[0,1] # means 0 position = 1st row, 1 position = 2nd column
# gives [row pos no, column pos no] => asking for give me the element of 1th row and 2st column

x[2,9] # [pos 2, pos 9] = [row 3, column 10] = means give the element of 3nd row & 10th colum match.

x[1] # means give the all elements in the 1st pos = row 2 all elements.

x[:,2] # [: , pos 2] = [all rows, column 3] = all rows 3rd column value will be returned.

x[1:3] # 1 is inclusive & 3 is exclusive = gives 1 and 2 pos = 2nd row & 3rd row

x[:,1:3] # [:,pos 1 pos 2] = all rows, 2nd column 3rd column = all rows matching 2nd, 3rd column values will be returned.

x[1:3,1:3] # [pos 1 pos 2, pos 1 pos 2] = [row 2 row3, column2 column3] = matching row 2 and 3 & column 2and 3 elements will be returned.

x[[0,3,9]] # From 2 dimentional array = Means its row operation = you are asking for pos0,pos3,pos9 = row1,row4,row10.

x[[0,3,9],2] # [pos0 pos3 pos9, pos2] = [row1 row4 row10, column3] = row 1,4,10 matching 2 column value will be returned

x[[0,3,9],[0,9,3]] # [pos0 pos3 pos9, pos0 pos9 pos3] = [row1 row4 row10, column1 column10 column4] = matching r1,r4,r10 & c1,c10,c4 values will be returned

#***** Boolean Indexing
bool_index = (x>50) #Apply the condition on all the elements & returned the true/false values for all the elements.
 
x[bool_index] # return the only values where the condition is true.

#********** Three dimentional array with in array
x = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[20,21,22],[23,24,25],[26,27,28]]])

x[0,0,0] = 100 # We modify the 0 indexing with 100 value
# (a,b,c) = (bunch pos,bunch row pos,bunch column pos) = (bunch1,row1,column1)

x[:,1,1] = 99 # [:,1,1]=[All bunches,row2,column2] = pickup all trays -> pickup up matching row2, column2 element and replace with 99 value.

x[0,:,:] = -888 # [0,:,:]=[first bunch,all rows, all columns] -> Pickup first tray and replace all rows and all column values with -888.




























