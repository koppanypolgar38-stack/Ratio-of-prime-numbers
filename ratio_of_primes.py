import matplotlib.pyplot as plt
import numpy as np
import random
import math

def is_prime(n):

  if n==2:
    return True

  elif n%2==0:
    return False

  else:
    for i in range(2,(n//2)+1):
      if n%i==0:
        return False
        break
    return True

def prime_list(n):
  l=[]
  for i in range(2,n+1):
    if is_prime(i)==True:
      l.append(i)
    else: continue
  return len(l)

def prime_ratio(n,k):
  l=[]
  for i in range(n,k+1):
    l.append(prime_list(i)/i)
  return l


x=np.linspace(2,100,200)
y=1/(np.log(x))

plt.figure(figsize=(12,8))
plt.plot([i for i in range(2,100)],prime_ratio(2,99))

plt.plot(x,y)
plt.grid(True)
plt.show()










