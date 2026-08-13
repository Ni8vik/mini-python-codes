def tbmm(k, num):
  n = 0
  for l in num:
    if l%k == 0:
      n +=1
    if len(num)== l:
      return True
    else:
      return False

def bemimim(n1:list):
  n = 0
  for i in range(1, min(n1)+1):
    if tbmm(i,n1) == True:
      n = i
      
  return n

print(bemimim(18,35))