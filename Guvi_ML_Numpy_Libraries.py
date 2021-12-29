#*************************************************************************
# PYTHON NUMPY
#*************************************************************************
import numpy as np
import random
import sys
list1=[10,20,30,40]
list2=[1,2,3,4]
numpy_array = np.array(list1)
numpy_array1 = np.array([list1,list2])
numpy_array1 = np.array([list1, list2], dtype=np.int32)
numpy_array2 = np.array([list1, list2], dtype=np.double)
print(numpy_array)
print('******')
print(numpy_array1)
print('******')
print(numpy_array2)
print('******')
na1 = np.random.random((4,5))
print(na1)
print('******')
na2 = na1.reshape((2,10))
print(na2)
print('******')
na = np.arange(1, 50, 3)
print(na)
print('******')
'''
na3 = np.arange(0,60,3)
print(na3)
na4 = na3.reshape((10,2))
print(na4)
# *********
table = []
for i in range(1,21):
    table.append(i*3)
nb = np.array(table)
print(nb)
res = nb.reshape(10,2)
print(nb.reshape(10,2))
print('******')
res_ad10 = res+10
print(res_ad10)
# *********
'''
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = a + b
print(c)
print('******')
na5 = np.empty([4,5])
print(na5)
print('******')
na6 = np.zeros([4,5])
print(na6)
print('******')
na7 = np.ones([4,3])
print(na7)
print('******')
na8 = na7*5
print(na8)
print('******')
'''
list3 = [1,2,3,4,5]
print("size of List list3 =",sys.getsizeof(list3) * len(list3))
list3_array = np.array(list3)
print("size of Numpy array list3_array =",sys.getsizeof(list3_array))
'''
list4=[1,2,3,4,5]
na9 = np.array(list4)
na9 = np.insert(list4,5,56)
print(na9)
print('******')





