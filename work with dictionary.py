def namlis(students):
    d = dict(input("nam va score bedid").split(":")for i in range(students))
    print(d)


namlis(4)

def sums(diton):
    newdic=0
    for key in diton:
        newdic+= int(diton[key])
    print(newdic)
    


mydict={'ali': '14', 'taha': '20', 'sara': '7'}
sums(mydict)


