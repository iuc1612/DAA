fin = open("Stock.txt")
prices_arr = []
data = fin.read()
l = data.split()
for line in l:
    prices_arr.append(line)
for i in range(0, len(l)):
    prices_arr[i] = int(float(prices_arr[i]))
print('ARRAY FROM THE FILE IS: ')
print(prices_arr)
print('--------------------------------------')



print("brute force")
print('--------------------------------------')
max=prices_arr[0]
for i in range (0, len(prices_arr)):
    if(prices_arr[i] > max):   
       max = prices_arr[i] 
print("Largest element present in given prices_arr: " ,max)
min=prices_arr[0]
for i in range(0,len(prices_arr)):
  if(prices_arr[i]<min):
    min = prices_arr[i]
print("Smallest element present in given prices_arr: " ,min)
print('--------------------------------------')

def minmax(i,j,min,max,):
 
  if(i==j):
    if(min>prices_arr[j]):
      min=prices_arr[j]
    if (max<prices_arr[i]):
      max=prices_arr[i]
    
    return min,max
  else:
   if (j==i-1):
     if (prices_arr[i]>prices_arr[j]):
       if max<prices_arr[j]:
         max=prices_arr[j] 
       if min>prices_arr[i]:
         min=prices_arr[i]
     else:
       if max<prices_arr[i]:
          max=prices_arr[i]
       if min>prices_arr[j]:
          min=prices_arr[j]
     return min,max
   else:
      mid=(i+j)//2
      min,max=minmax(i,mid,min,max)
      min,max=minmax(mid+1,j,min,max)

      return min,max


min,max=minmax(0, len(prices_arr)-1,99999,0)

print("divide and conquer")
print('--------------------------------------')
print("max element is:",max)
print("min element is:",min)