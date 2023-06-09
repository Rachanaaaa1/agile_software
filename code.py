for i in range(1,7):
    print(i)

for i in range(0, -5, -1):
    print(i)
    
for i in range(1, 12, 2):
    print(i)

for i in range(9, -4, -3):
    print(i)

#Write a Python program to find the sum of all even elements in a list
def find_sum(arr):
  sum=0
  for i in arr:
    if i%2==0:
      sum=sum+i
  return sum

arr=[1,2,4,6,8,9]
print(find_sum(arr))
