
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
 
  dynamic programming tabulation technique gives time complexicity of O(n*k)
  and space complexicity of O(n*k)

  space efficiency algorithm:
  above dynamic program will generate pascals triangle:
  n=0 | 1 
  n=1 |1 1
  n=2 |1 2 1
  n=3 |1 3 3 1 
  n=4 |1 4 6 4 1
  ..........
  
  we can observe at any n, we can construct n+1 row if we have data for nth row .example
  at n = 2 
  A(n) = [1, 2, 1, 0]
  at any location, in the (n+1)th we write as follows
  A(n+1) = [1, 2, 1,0]
  A(n+1)[i]  = A(n+1)[i] + A(n+1)[i-1] 
  so, A(n+1)[3] = A(n+1)[3] + A(n+1)[2] = 0+1 = 1
      A(n+1)[2] = A(n+1)[2] + A(n+1)[1] = 1+2 = 3
      A(n+1)[1] = A(n+1)[1] + A(n+1)[0] = 2+1 = 3
      
   so, the A(n+1) = [1,3,3,1]
    here the time complexicity is O(n*k) and the space complexicity is O(k). so space efficient solution
  
'''



def coeff(n ,k ):
 table = [0 for x in range(k+1)] # n+1 x  k+1 sized table
 
 table[0] = 1
 for i in range(1, n+1):
  for j in range(min(i, k), 0, -1):
    table[j] = table[j] + table[j-1]
 return table[k]   
 
n, k= raw_input().split(' ')
n, k = int(n), int(k)
print "c({}, {}):{}".format(n, k, coeff(n,k)) 
