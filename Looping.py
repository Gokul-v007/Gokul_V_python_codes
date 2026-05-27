
#Question 1: Print Numbers from 1 to N
n=int(input())
for i in range(1,n+1):
   print(i,end='')

#Question 2: Print Even Numbers up to N
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i,end='')

#Question 3: Sum of First N Natural Numbers
n=int(input())
s=0
for i in range(1,n+1):
    s+=i
print(s)

#Question 4: Multiplication Table
n=int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#Question 5: Factorial of a Number
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#Question 6: Count Digits in a Number
n=int(input())
c=0
while n>0:
    digit=n%10
    c+=1
    n=n//10
print(c)

#Question 7: Reverse a Number
n=int(input())
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)

#Question 8: Sum of Digits
n=int(input())
s=0
while n>0:
    digit=n%10
    s+=digit
    n=n//10
print(s)

#Question 9: Print Squares from 1 to N
n=int(input())
for i in range(1,n+1):
    print(i**2,end=' ')

#Question 10: Print Odd Numbers in a Range
a,b=map(int,input().split())
for i in range(a,b+1):
    if i%2!=0:
        print(i,end='')
        
#Question 11: Number Divisors
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end='')
        
        
#Question 12: Check Prime Number
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not prime")


#Question 13: Simple Star Line Pattern
n=int(input())
for i in range(n):
    print("*",end='')
#Question 14: Increasing Number Pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    
#Question 15: Calculate Power
a,b=map(int,input().split())
print(a**b)

# Medium looping 



# 1. ATM Withdrawal Feasibility Checker
n = int(input())

vr = 0
ivar = 0
tot = 0
for i in range(n):
    amount = int(input())
    if amount>0 and amount%100==0:
        vr+=1
        tot+=amount
    else:
        ivar+=1
print("Valid request :",vr)
print("Ivalid reqest :",ivar)
print("Total amount :",tot)   
