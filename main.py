
''' 
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
def exo1(begin: int, end : int):
  solution = []
  for i in range(begin, end + 1):
     if i % 7 == 0 and i % 5 != 0:
       solution.append(i)
  print(solution)               
 exo1(2000, 3200)

 l=[]
 for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

 print('a:'.join(l))
 '''
'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
n=int(input("enter the integer number : "))
s=1
for i in range(n,1,-1):
    s*=i
print (s)
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))'''
<<<<<<< HEAD
=======
n=int(input("enter the integer : "))
exo_2={}
for i in range (1,n+1):
  exo_2[i]=i*i
print (f'the output is : {exo_2}')
>>>>>>> b11634c (exo_3 done)
