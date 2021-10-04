n=int(input("Enter a number:"))
copy=n
r=0
while n>0:
  rem=n%10
  r=r*10+rem
  n=n//10
if(copy==r):
    print("PALINDROME")
else:
  print("NOT PALINDROME")
