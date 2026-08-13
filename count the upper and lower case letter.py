s='I Love You'
u="The Story Remain"
def supe(s):
    upter={"u":0, "l":0}
    for i  in s:
        if i.isupper():
            upter["u"] += 1
        elif i.islower():
            upter["l"] += 1
    print(upter)
    
supe(s)
supe(u)