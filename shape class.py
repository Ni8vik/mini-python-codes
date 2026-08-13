star = "*"

class shapes:
    global star
    #parallelogram
    def  parallelogram(self, times):
        
        for i in range(times):
            print(i*" " + (10*star))
            
    #triangle    
    def triangle(self, times):
        for i in range(times*2):
            if i%2!=0:
                print(f"{star*i:^20}")
    #square
    def square(self, times):
        
        for i in range(times):
            print(f"{star*6:^20}")
            
tywant=int(input("how many times you want?  "))
shapes.parallelogram(None, tywant)