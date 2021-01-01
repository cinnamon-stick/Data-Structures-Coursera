## FIBONACCI WITH DYNAMIC PROGRAMMING ##
def fibonacci(number:int,valuesSolved:dict)->int: 
  if number<=1:
    return number

  if not str(number-1) in valuesSolved:
    valuesSolved.update({str(number-1):fibonacci(number-1,valuesSolved)})

  if not str(number-2) in valuesSolved:
    valuesSolved.update({str(number-2):fibonacci(number-2,valuesSolved)})
    
  return valuesSolved[str(number-1)]+valuesSolved[str(number-2)]

for i in range(0,40):
  print(fibonacci(i,{}))
