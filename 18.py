def is_prime(n):
  if(n>1):
    for i in range(2,int(n/2)+1):
      if n%i==0:
        print(n,"NOT PRIME")
        break
      else:
        print(n,"PRIME")
        break
  else:
    print(n,"NOT PRIME")

is_prime(11)
is_prime(16)
