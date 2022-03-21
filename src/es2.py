def myfunc():
  import numpy as np
  import math
  matrix=np.loadtxt("es2_data_python_5.txt",dtype="f",delimiter=None)
  
  sumax=0.0
  sumin=0.0
  
  for i in range(len(matrix)-1):
    sumin= sumin + matrix[i][2]

  aveTmin=1/(len(matrix))*sumin

  for i in range(len(matrix)-1):
    sumax= sumax + matrix[i][3]

  aveTmax=1/(len(matrix))*sumax

  qqmin=0.0
  qqmax=0.0

  for i in range(len(matrix)-1):
    qqmin=qqmin+(matrix[i][2]-aveTmin)**2

  for i in range(len(matrix)-1):
    qqmax=qqmax+(matrix[i][3]-aveTmax)**2

  varmin=(1/(len(matrix)-1))*qqmin
  varmax=(1/(len(matrix)-1))*qqmax

  print("Varianza (no lib) minime :",varmin)
  print("Varianza (no lib) massime :",varmax)

  devmin=math.sqrt(varmin)
  devmax=math.sqrt(varmax)

  print("devmin (no lib):",devmin)
  print("devmax (no lib):",devmax)

  varray=np.var(matrix,axis=0)
  print("Varianze stimate con libreria:", varray[2],varray[3])
  print("Devstd stimate con libreria:", math.sqrt(varray[2]),math.sqrt(varray[3]))
  

myfunc()