'''
 
Minimum steps to minimize n as per given condition

Given a number n, count minimum steps to minimize it to 1 according to the following criteria:

    If n is divisible by 2 then we may reduce n to n/2.
    If n is divisible by 3 then you may reduce n to n/3.
    Decrement n by 1.


  brute-force solution:
  time complexicity: O(3^n)
'''
def min_steps(n):
 if n == 0 or n==1:
  return n

 if n == 2 or n == 3:
  return 1

 if n%3 ==0 and n%2 ==0:
  return 1+min(min_steps(n/3), min_steps(n/2), min_steps(n-1))
 elif n%3 == 0:
  return 1 + min(min_steps(n/3), min_steps(n-1))
 elif n%2 == 0:
  return 1+min(min_steps(n/2), min_steps(n-1))
 return 1+min_steps(n-1) 


n = int(raw_input())
print "no.of steps:{}".format(min_steps(n))
