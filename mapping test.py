
def fibbbonachi():
      a , b = 0, 1
      while True:
            yield a 
            a, b = b, a+b
fib =   fibbbonachi()   
for _ in range(10):
      print(next(fib))