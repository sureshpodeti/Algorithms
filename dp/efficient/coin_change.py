'''
  We have given plenty of coins of differnt denomination, we need to find out the 
  # of ways to make a sum N.
  eg: s ={1,2,3} these are avaible demoniations (assume we have plenty of such each coin)
   we need to make sum N= 4
     solution:
            {1,1,1,1}, {1,2,1}, {1,3}, {2,2}
            so, there are four solutions.

        Let f(s, m, N) denote the # ways to make 'N' from 'm' given coins
        f(s, m, N) = f(s, m, N-A[m-1])                 +     f(s, m-1, N) 
                    solutions that contain mth coin          solution that dont contain 'm'th coin
          eg: solution of the problem = solution that contain coin has 3 value + solution that dont contain coin 3
                                      =  1 (i.e {1,3})        + 3 (i,e {1,1,1,1}, {1,2,1}, {2,2})  = 4 

       Time complexicity: 
           T(s, m, N) = T(s, m, N-A[m-1]) + T(s, m-1, N)
           O(2^n)
   
       dynamic programming approach:
               time complexicity: O(m*n), m = #of coins, N = sum to make
'''


def coin_change(A, m, N):
 s = [[0 for i in range(m+1)] for x in range(N+1)]

 # first row, N = 0, intialize row with all 0's
 for i in range(m+1):
  s[0][i] = 1
 
 for i in range(N+1):
  s[i][0] = 0

 for i in range(1, N+1):
  for j in range(1, m+1):
   if i >= A[j-1]:
    s[i][j] =s[i-A[j-1]][j] + s[i][j-1]
   else:
    s[i][j] = s[i][j-1]
   
 return s[N][m]




s = raw_input().split(' ')
s = map(int ,s)
N = int(raw_input())

print "coin_change({},{}):{}".format(s, N, coin_change(s, len(s), N))
