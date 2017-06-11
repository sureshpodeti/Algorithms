
# _*_ coding: utf-8 _*_
'''
 Bionomial coffienent

            n
 (1+x)^n =  Σ nCi * x^i
            i =0

  Let f(n,k) gives the coeffiecent of kth term. 
  f(n,k) = nCk = n! /(k! * (n-k)!)

  solution:
  f(n,k) can be written as following:
   f(n,k) = f(n-1, k-1) + f(n-1, k)
  base case: f(n, k) =1 if k ==0 or k==n
  
  T(n,k) = T(n-1, k-1) + T(n-1, k) + C
  Time complexicity would be O(2^n)
'''



def coeff(n ,k ):
 # base case 
 if k == 0 or k == n:
  return 1
 return coeff(n-1, k-1) + coeff(n-1, k)


n, k= raw_input().split(' ')
n, k = int(n), int(k)
print "c({}, {}):{}".format(n, k, coeff(n,k)) 
