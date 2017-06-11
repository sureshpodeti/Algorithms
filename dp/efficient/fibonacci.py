#_*_ coding:utf-8 _*_
'''
 Fibonacci problem:
 F = {0, 1,1,2,3,5,8,13, ...}
 F(i) = F(i-1) + F(i-2) ∀i  ∈ Z>=0 (positive integers including 0) 
 
 Recursive brute force approch gives time complexicity of O(2^n)
 dynamic programming tabulation gives time complexicity of O(n)
 following approach is the efficent one with time complexicity of O(log(n))

 F = [[1,1], [1,0]]
 F^n = [[F(n+1), f(n)], [f(n), f(n-1)]]
 so,
 F^(n-1) = M = [[F(n), f(n-1)], [f(n-1), f(n-2)]]  
 M[0][0] Gives the nth fibonacci number. 
 
'''



def fib(n):
 if n==0 or n==1:
  return n
 F = [[1,1], [1,0]]
 power(F,n-1)
 return F[0][0]

def power(F, n):
 if n==0 or n==1:
  return
 M = [[1,1], [1,0]]
 power(F, n/2)
 multiply(F,F)
 if n%2 !=0:
  multiply(F,M)

def multiply(F, M):
 x = F[0][0]*M[0][0] + F[0][1]*M[1][0]
 y = F[0][0]*M[0][1] + F[0][1]*M[1][1]
 z = F[1][0]*M[0][0] + F[1][1]*M[1][0]
 w = F[1][0]*M[0][1] + F[1][1]*M[1][1]
 
 F[0][0] = x
 F[0][1] = y
 F[1][0] = z
 F[1][1] = w

 

n = int(raw_input())
print "fib({}):{}".format(n, fib(n))
