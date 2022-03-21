import numpy as np
a=np.array([1,2,3])
b=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
c=np.arange(5,dtype="f")
d=np.array([3,2,5,6,7])

print("1Slice",a[1])
print("2Slice")
print(b[1:,0:3])
print("3Slice")
print(b[1:,1])

print("c",c)
print("d",d)
c=d
print("c copy by reference da d", c)
d[0]=67
print("c copy by reference dopo aver cambiato un valore in d", c)

a=d.copy()
print("a copy by value da d",c)
a[0]=989
print("a dopo aver cambiato valore di un elemento",a)