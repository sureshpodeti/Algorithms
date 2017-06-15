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
'''


def coin_change(s, m, N):
 if N == 0 :
  return 1
 
 if N <0:
  return 0
 
 if m==0 and N>=1:
  return 0
  
 return coin_change(s, m, N-s[m-1]) + coin_change(s, m-1, N)




s = raw_input().split(' ')
s = map(int ,s)
N = int(raw_input())

print "coin_change({},{}):{}".format(s, N, coin_change(s, len(s), N))
