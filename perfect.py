n=int(input ("enter a number"))
sum_of_factors=0
print("factors(excluding itself):",end=" ")
for i in range (1,n):
 if n%i==0:
  print(i,end-" ")
 sum_of_factors+=i
 printf("\n sum of factors:",sum_of_factors)
  if sum_of_factors==0:
   print(n,"is a perfect number")
  else:
   print(n,"is not a perfect number.")
