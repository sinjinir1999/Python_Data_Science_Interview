l=[1,2,3,4,12,33,12,20]
e=0
o=0
for i in range(0,len(l)):
  if l[i]%2==0:
    e=e+1
  else:
    o=o+1
print(e)
print(o)
