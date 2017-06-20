'''
 
Minimum steps to minimize n as per given condition

Given a number n, count minimum steps to minimize it to 1 according to the following criteria:

    If n is divisible by 2 then we may reduce n to n/2.
    If n is divisible by 3 then you may reduce n to n/3.
    Decrement n by 1.


  dynamic programming technique:
   time complexicity: O(n)
   space complexicity: O(n)
'''
def min_steps(n):
 s = [0]*(n+1)
 s[0] = 0
 s[1] = 0
 s[2] =1
 s[3] =1
 
 for i in range(4, n+1): 
  if i%3 ==0 and i%2 ==0:
   s[i] =  1+min(s[i/3], s[i/2], s[i-1])
  elif i%3 == 0:
   s[i] = 1 + min(s[i/3], s[i-1])
  elif i%2 == 0:
   s[i] =  1+min(s[i/2], s[i-1])
  else:
   s[i] =  1+s[i-1] 

 return s[n]

n = int(raw_input())
print "no.of steps:{}".format(min_steps(n))
