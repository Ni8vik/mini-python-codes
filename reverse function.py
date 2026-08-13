#string or number
num = 2371769683
#reverse func
x =reversed(str(num))
y= (str(elm) for elm in x)
sep = ""
fin = sep.join(y)

print(x)