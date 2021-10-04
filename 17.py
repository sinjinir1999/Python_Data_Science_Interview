l=[1,2,3,4,6,7,9,8]
even=[]
odd=[]
for i in l:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)

print(even)
print(odd)
