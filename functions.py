#Function WITHOUT input & WITHOUT return
#1.print 1 to 10
def number():
    for i in range(1,11,1):
        print(i)
number()
#__________________________________________________________________________________
#2.Print even numbers
def even():
    for i in range(1,21,1):
        if(i%2==0):
            print(i)
even()
#____________________________________________________________________________________________________
# 3.Print odd numbers
def odd():
    for i in range(1,21,1):
        if(i%2!=0):
            print(i)
odd()
#___________________________________________________________________________________________________
# 4. Print multiplication table of 5
def table():
    n=5
    for i in range(1,11,1):
        mul=n*i
        print(f"{n}*{i}=",mul)
table()
#____________________________________________________________________________
# 5. Sum of 1 to 10
def sumOfnumbers():
    sum=0
    for i in range(1,11,1):
        sum=sum+i
    print(sum)
sumOfnumbers()
#______________________________________________________________________
# 6. Factors of 24
def fact():
    n=24
    for i in range(1,n+1,1):
        if n%i==0:
            print(i)
fact()
#_____________________________________________________________________
# 7. Check prime number
def prime():
    n=29
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
    if count==2:
        print(n,"is prime")
    else:
        print(n,"is not prime")
prime()
#_________________________________________________________________________
# 8. Reverse a number
def reverse():
    n=12345
    rev=0
    while n!=0:
        ld=n%10
        rev=rev*10+ld
        n=n//10
    print(rev)
reverse()
#_______________________________________________________________________
# 9. Palindrome number
def palindrome():
    n=525
    newNum=n
    rev=0
    while n!=0:
        ld=n%10
        rev=rev*10+ld
        n=n//10
    if newNum==rev:
       print(newNum,"is palindrome")
    else:
        print(newNum,"is not palindrome")
palindrome()
#___________________________________________________________________________
# 10. Prime numbers from 1 to 100
def primeNumbers():
    for j in range(1,101,1):
        count=0
        n=j
        for i in range(1,n+1,1):
            if n%i==0:
                count=count+1
        if count==2:
            print(n)
primeNumbers()
#______________________________________________________________________________
#2️. Function WITH input & WITHOUT return

# 1. Square of a number
def square(num):
    print(num*num)
square(5)
# #_________________________________________________________________________
# 2. Even or Odd
def evenOdd(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
evenOdd(10)
#__________________________________________________________________________
# 3.Factorial
def  factorial(n):
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
    print(fact)
factorial(7)
#__________________________________________________________________________
# 4.Sum of digits
def digitSum(n):
    sum=0
    while n!=0:
        ld=n%10
        sum=sum+ld
        n=n//10
    print(sum)
digitSum(7539)
#__________________________________________________________________________
# 5.Count digits
def digitCount(n):
    count=0
    while n!=0:
        ld=n%10
        count=count+1
        n=n//10
    print(count)
digitCount(5678943)
#______________________________________________________________________________
#6. Largest digit
def largestdigit(n):
    large=0
    while n!=0:
        ld=n%10
        if ld>large:
          large=ld
        n=n//10
    print(large)
largestdigit(865965)
#______________________________________________________________________
# 7.Smallest digit
def smallestdigit(n):
    small=9
    while n!=0:
        ld=n%10
        if ld<small:
            small=ld
        n=n//10
    print(small)
smallestdigit(76345672)
#_____________________________________________________________________
# 8.Palindrome
def palindrome(n):
    newnum=n
    rev=0
    while n!=0:
        ld=n%10
        rev=rev*10+ld
        n=n//10
    if newnum==rev:
        print(newnum,"is palindrome")
    else:
        print(newnum,"is Not palindrome")
palindrome(15651)
#_______________________________________________________________________
# 9. Perfect number
def perfectNumber(n):
    sum=0
    for i in range(1,n,1):
        if n%i==0:
            sum=sum+i
    if sum==n:
            print(n,"is a perfect number")
    else:
            print(n,"is not a perfect number")
perfectNumber(28)
#_____________________________________________________________________
# 10. Difference between largest and smallest digit
def difference(n):
    max=0
    min=9
    while n!=0:
        ld=n%10
        if ld>max:
            max=ld
        if ld<min:
            min=ld
        n=n//10
    print("Difference between largest and smallest digit is :",max-min)
difference(987234)
#_________________________________________________________________________
# 3 WITHOUT INPUT & WITH RETURN
# 1. Count Even and Odd Digits
def countevenOrodd():
    n=5678534
    even=0
    odd=0
    while n!=0:
        ld=n%10
        if ld%2==0:
            even=even+1
        else:
            odd=odd+1
        n=n//10
    return even,odd
result=countevenOrodd()
print("Even digits=",result[0])
print("Odd digits=",result[1]) 
#______________________________________________________
# 2.Sum of Digits
def digitSum():
    n=78643
    sum=0
    while n!=0:
        ld=n%10
        sum=sum+ld
        n=n//10
    return sum
result=digitSum()
print(result)
#__________________________________________________________________________
# 3. Reverse a Number
def reverseNumber():
    n=1506
    rev=0
    while n!=0:
        ld=n%10
        rev=rev*10+ld
        n=n//10
    return rev
result=reverseNumber()
print("reverse of 1506 is",result)
#___________________________________________________________________
#4. Palindrome Number
def palindromeNumber():
    n=5665
    newNum=n
    rev=0
    while n!=0:
        ld=n%10
        rev=rev*10+ld
        n=n//10
    if newNum==rev:
        return "is Palindrome"
    else:
        return "Not Palindrome"
result=palindromeNumber()
print(result)
#__________________________________________________________________________
# 5. Digit Frequency
# Find how many times a particular digit occurs.
def digitFrequency():
    n=1223342
    search=2
    count=0
    while n!=0:
        ld=n%10
        if ld==search:
            count=count+1
        n=n//10
    return count
result=digitFrequency()
print("Digit Frequency of 2 =",result)
#____________________________________________________________________
# 6.Second Largest Digit
def secondLargest():
    n=583921
    large=0
    second=0
    while n!=0:
        ld=n%10
        if ld>large:
            large=ld
        n=n//10
        if ld<large and ld>second:
            second=ld
        n=n//10
    return second
print("Second largest digit=",secondLargest())
#_____________________________________________________________________
# 7.Product of Digits
def productOfDigits():
    n=2345
    product=1
    while n!=0:
        ld=n%10
        product=product*ld
        n=n//10
    return product
result=productOfDigits()
print("Product of Digits =",result)
#__________________________________________________________________________
#8.Count Factors
def countFactors():
    n=36
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
    return count
result=countFactors()
print("Number of factors=",result)
#______________________________________________________________________
#9.LCM of Two Numbers
def lcm():
    a=12
    b=18
    if a>b:
        large=a
    else:
        large=b
    while True:
        if large%a==0 and large%b==0:
            return large
        large=large+1
result=lcm()
print("LCM of 12 and 18 =",result)
#_______________________________________________________________________
#10.swap to 2 numbers
def swapNumbers():
    a,b=(10,20)
    a=a+b
    b=a-b
    a=a-b
    return a,b
result=swapNumbers()
print(result)
#_________________________________________________________________________