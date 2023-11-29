import numpy as np


a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(a)
print(a[1,1])

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)
print(l1*5)
print(a1*5)

print(l1+l2)
print(a1+5)
print(a1+a2)

a3 = np.array([1,2,3])
a4 = np.array([[1],[2]])

print(a3+a4)

ar1 = np.array([[1,2,3],[4,5,6]])
print(ar1)
ar1 = np.delete(ar1,1,1)
print(ar1)

a11 = np.array([[1,2,3,4,5,6,7,8],
                [9,10,11,12,13,14,15,16],
                [17,18,19,20,21,22,23,24],
                [25,26,27,28,29,30,31,32]])
print(a11)
print(a11.size)
print(a11.shape)
#print(np.reshape(a11,(20)))
#print(np.reshape(a11,(2,5,2)))
#print(np.reshape(a11,(2,2,5)))
print(np.split(a11,2,axis=0 ))
print(np.split(a11,4,axis=0 ))
print(np.split(a11,2,axis=1 ))