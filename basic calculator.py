def michine(a, b, c):
    if c ==1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    else: return a/b
print("1: sum \n2: sub \n3: mul \n4: div")
s=int(input("Enter your selection"))
def main():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(michine(a,b,s))
main()