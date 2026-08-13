#sums of two list
    # a=[1, 2, 3, 4, 5]
    #b=[10, 11, 12, 13, 14, 15]
    #print(list(zip(a, b)))
    #def sums(a, b):
        #print([i+j for i, j in zip(a, b)    ])
    ##sums(a,b)


#pascal pyramid
def f(row, a, b):
    lst=[1]
    for i in range(row):
        print(lst)
        lst=[j+k for j,k in zip(lst+a, b+lst)]
        
    print(lst)
f(16,[0],[0])


#i cant understand the code above