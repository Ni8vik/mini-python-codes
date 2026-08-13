def prime(renge= 100):    
      
      primes= [True] * (renge+1)   
      primes[0] = primes[1] = False
      
      for i in range(2, renge+1):
            if primes[i]:
                  yield i
                  for j in range(i*i, renge+1, i):
                        primes[j] = False
                              

for j in prime():
      print(j)