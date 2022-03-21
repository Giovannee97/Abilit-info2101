def crea_istogramma():
  
  import numpy as np
  a=np.loadtxt("mydata.txt",dtype='i',delimiter=",")

  x=[]

  for i in range(len(a)):
    x.append(a[i]*("*"))

  for i in range(len(x)):
    print(x[i])
  

crea_istogramma()