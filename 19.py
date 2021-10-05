def fibonacci(n):
  a=0
  b=1
  if(n<0):
    return -1
  if(n==0):
    return a
  if(n==1):
    return 1
  else:
    for i in range(2,n):
      c=a+b
      a=b
      b=c
    return b
  
  fibonacci(9)
