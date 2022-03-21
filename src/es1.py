def crea_istogramma():
  
  import numpy as np
  import matplotlib.pyplot as plt
  a=np.loadtxt("mydata.txt",dtype='i',delimiter=",")

  x=[]

  for i in range(len(a)):
    x.append(a[i]*("*"))

  for i in range(len(x)):
    print(x[i])

  plt.hist(a,len(a))
  

crea_istogramma()