import re

def isMatch(s, p):
      
      if 0<len(s)<=20 and 0<len(p)<=20:
            
            if any(not(c.isalpha() or c == "." or c=="*") for c in p):
                  return "the pattern or the string can only have character, dots or *" 
            
            else:
                  if all((j.islower() or j=="." or j=="*") for j in p):
                 
                        result = re.fullmatch(p, s)
                  
                        if result:
                              return True
                        
                        else:
                              return False
                        
                  else:
                        return "the pattern have to be lower case and don't have special character exept dot and * "
      else:
            return "please resize the input! 0<input<=20"
