#_*_ coding:utf-8 _*_
'''
 Ugly number:
 Given a number n, we need to return the nth ugly number
 ugly number ∈ {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …}

 Ugly numbers are numbers whose only prime factors are 2, 3 or 5
 U[0] = 1, U[1] = 2, U[2] = 3 ... , U[n] = ???
 
 each number formed by:
  1 --> 1x2 = 2, 1x3 = 3, 1x5 =5
   so, 1 forms [2,3,5]

 2 --> 2x2 =4, 2x3 = 6, 2x5 = 10
  so, 2 forms [4,6,10]

 like that series goes on


 dynamic programming approach:
  time complexicity: O(n)
  space complexicity: O(n)


'''
def ugly_num(N):
 s = [None]*(N+1)

 s[0] = 1
 i2 = i3 = i5 = 0
 for j in range(1, N+1):
   s[j] = min(s[i2]*2,
              s[i3]*3,
              s[i5]*5
             )
   if s[j] == s[i2]*2:
     i2 += 1
   if s[j] == s[i3]*3:
    i3 += 1
   if s[j] == s[i5]*5:
    i5 += 1
 
 return s[N]

N = int(raw_input())
print "ugly_num({}):{}".format(N, ugly_num(N))
