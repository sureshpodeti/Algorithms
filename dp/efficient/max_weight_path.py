'''
 Given a matrix consiting of integers , we need to figure out the max weight path(starts from (0,0) and
 ends at any element in the last row)

 time complexicity: O(m*n) mxn sized matrix
 space complexicity: O(m*n)
'''





def max_weight_path(A, m, n):
 s = [[0 for i in range(n+1) ]for x in range(m+1)]
 
 for i in range(m+1):
  for j in range(n+1):
   if i==0:
    s[i][j] = 0
   elif i == 1:
    s[i][j] = A[i-1][j-1]
   elif j>i:
    s[i][j] = 0
   else:
    s[i][j] = max( s[i-1][j-1],
                   s[i-1][j]) + A[i-1][j-1]
 
 return max(s[m])


M = [[ 4, 2 ,3 ,4 ,1 ],
    [ 2 , 9 ,1 ,10 ,5 ],
    [15, 1 ,3 , 0 ,20 ],
    [16 ,92, 41, 44 ,1],
    [8, 142, 6, 4, 8] 
    ]

print "max_weight:{}".format(max_weight_path(M, 5, 5))
