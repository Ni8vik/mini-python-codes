def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)
    
s=int(input("Enter a nuber that you want to factorialaze:  "))    
print(factorial(s))