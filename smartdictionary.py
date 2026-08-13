#time spent 5h
#this fuking thing dosen't work
 
    
groups = {"a":["a","ap","app","apply","apple","appl"],
          "b":["b","ba","ban","bana","banan","banana"]}

#extract the value into a list
def extract(x=groups):
        
        extracted=[]
      
        
        for i,j in x.items():
               extracted.append(sorted(j))
               
        
        return extracted

#seperate each word into a list
def seperations():
        sortedlst=[]
        persorted= []
        smt = []
        for i in (extract()):
                 
                for j in i:
                
                        for k in j:
                                ed = k.split(", ")
                                persorted.append(ed)
                        
                        sortedlst.append(persorted) 
                        persorted = []
                                      
        return sortedlst
def extractdigit(v, z= extract()):
        
        if len(z) == 0:
                return
        print(z)
        extractdigit(z[:-1])
        
#check for subsets of string/list
def subsets(y=seperations()):
        #print(y)
        smt = [] # short memory term
        psbltngs= []
        deleted = []
        
        for i in y:
                for j in i:
                        indexes = i.index(j)
                        psbltngs.append(j)
                        
                        if j in i:
                                while j in i:
                                        if i[indexes] in i:
                                                i.pop(indexes)
                        #i.pop(indexes)                
                        print(j)
        print(psbltngs)
                        
               
                     
                               
                                
                        
        
       
                 
        
        





#print(extract())
#print(seperations())
print(extractdigit(3))
#print(subsets())
