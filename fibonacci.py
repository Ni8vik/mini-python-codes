def fibonachi(x):
    if x in [0,1]:
        return x
    return fibonachi(x-1) + fibonachi(x-2)
    
if __name__ == "__main__":
    c=int(input("Please enter how many times do you want your number: "))
    print(list(fibonachi(x) for x in range (c+1)))