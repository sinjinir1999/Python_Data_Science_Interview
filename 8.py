def prod_of_digits(n):
  prod=1
  while(n>0):
    prod=prod*(n%10)
    n=n//10
  print(prod)
prod_of_digits(243)
