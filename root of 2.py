def baseof2(n, t=2):
    for i in range(n+1):
        print(t**i, end="\t")

def sum(n, t):
    s=0
    for i in range(n+1):
        s+= t ** i 
    print(s)


nums=int(input("how many time to generate"))
times=int(input("whats the root to generate"))
baseof2(nums, times)
do=input("do you want to generate the sum")
if do=="yes":
    sum(nums, times)
elif do=="no":
    print("ok")
else:
    print("i dont under stand")