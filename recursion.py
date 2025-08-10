#printing the name N times
def printNtimes(i,name):
      if i != 0 :
            print(name)
            printNtimes(i-1,name)

      else:
            return 0 
      
name = input("enter a name: ")
printNtimes(5,name)
    
#printing the name one to n
def printoneton(j,n):
      if j != n+1:
            print(j)
            printoneton(j+1,n)
      else:
            return 0 
      
j = 1
n = int(input("enter n "))
printoneton(j,n)
#to print n to 1
def printntone(n):
      if n != 0:
            print(n)
            printntone(n-1)
      else:
            return 0 
      

n = int(input("enter n "))
printntone(n)

#Sum of first natural numbers
sums = 0
def sumof(j,n):
      global sums
      if j != n+1:
            sums += j
            sumof(j+1,n)

            

      else:
            return 0 
      
   
sumof(1,5)


print(sums)
#factorial of a number
product = 1
def fact(n):
      global product
      if n > 0:
            product = product * n 
            fact(n-1)


n = 5
fact(n)

print(product)

#Reverse an array 
def reversearray(n,arr,new):
      
      if n >= 0:
            new.append(arr[n])
            reversearray(n-1,arr,new)
      
      else:
            return 0


arr  = [1,2,3,4,5]
n = 4
new = []
reversearray(n,arr,new)
print(new)



      
