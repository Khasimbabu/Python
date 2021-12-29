'''
def mean(someList):
    total = 0
    for a in someList:
        total += float(a)
    mean = total/len(someList)
    return mean
def standDev(someList):
    listMean = mean(someList)
    dev = 0.0
    for i in range(len(someList)):
        dev += (someList[i]-listMean)**2
    dev = dev**(1/2.0)
    return dev
def correlCo(someList1, someList2):

    # First establish the means and standard deviations for both lists.
    xMean = mean(someList1)
    yMean = mean(someList2)
    xStandDev = standDev(someList1)
    yStandDev = standDev(someList2)
    # r numerator
    rNum = 0.0
    for i in range(len(someList1)):
        rNum += (someList1[i]-xMean)*(someList2[i]-yMean)

    # r denominator
    rDen = xStandDev * yStandDev

    r =  rNum/rDen
    return r

print(correlCo([1, 2, 3, 4, 5], [6, 9, 12, 15, 18]))
'''
'''
from scipy.stats.stats import pearsonr
a = [1, 2, 3, 4, 5]
b = [6, 9, 12, 15, 18]
print(pearsonr(a,b))
'''
import numpy as np

a = np.ones([2,2]) * 8
print(a)
a1 = np.random.random([3,3])
print(a1)
print(a1.sum())
print(a1.mean())
print(a1.max())
print(a1.min())
y = np.arange(1,36)
print(y)
print(y.ndim)
n=y.reshape([5, 7])
print(n)

print(n[2:4,:])
print(n[:,2:7:2])

a = np.array([4.,2.])
b = np.array([3.,8.])
h_stack = np.hstack((a,b))
v_stack = np.vstack((a,b))
print(h_stack)
print(v_stack)

arr = np.array([[5,12,51,25] ,[25,29,2,27]])
print(arr)
max_idx = np.argmax(arr)
min_idx = np.argmin(arr)
print(max_idx,min_idx)

max_col = np.argmax(arr,axis = 0)
min_col = np.argmin(arr,axis = 0)
print (max_col,min_col)

max_row = np.argmax(arr,axis = 1)
min_row = np.argmin(arr,axis = 1)
print (max_row,min_row)
#0,1,1,2,3,5,8,...,(n-2),(n-1),n
'''
def feb(n):
    if(n<=1):
        return n
    else:
        return (feb(n-1)+feb(n-2))
count=10
for i in range(count):
    print(feb(i))
'''
div_by_four_lc = [num for num in range(200) if num%4==0]
print(div_by_four_lc)

