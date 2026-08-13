def n(num: int, times: int, find):
  numbers = [num]
  finded = 0
  
  for i in range(times):
    
    num = (num+1)/4
    numbers.append(num)
    
  for j in numbers:
    
      if j < find:
        finded = numbers.index(j)
        break    
      
  return numbers, finded

print(n(8, 5, 0.6))