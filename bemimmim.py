def bemimim(x,y):
    
    if 0 in(x,y):
        print("the bimimim is: "+ str(x))
    else:
        return bemimim(y, x % y)
        
#print(bemimim (107,24))
    