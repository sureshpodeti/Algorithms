'''
 Given two strings X, Y  and two no.s 'cosx', 'cosy' as there cost incurred if we delete
 each time in respective strings

 Task is to figure out the min cost to make strings identical

 eg: X = 'abcd'  , Y= 'acdb' , costx = 10, costy = 20
  output = 30


  brute-force algorithm:
    Let f(i, j) denote the min cost to make strings identical. i = |X|-1 , j = |Y|-1
             
                f(i-1, j-1)      if X[i] == Y[j]
    f(i, j) = 

               min{costx+ f(i-1, j), costy+f(i, j-1)}     ,otherwise

    base case: 
           if i < 0 and  j < 0:
             return 0
                
           if i<0 then 
              return  cosy*(j+1)

           if j<0 then 
             return cosx*(i+1)
    
   time complexicity: O(2^n)

   dynamic programming technique:
      time complexicity: O(mn) where m = |X|, n = |Y|
'''
def min_cost(x, y, costx, costy):

 s = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]

 # intialize the first row
 for i in range(1, len(y)+1):
  s[0][i] = i*costy

 # intialize the first column
 for i in range(1, len(x)+1):
  s[i][0] =i*costx
 
 # fill rest matrix
 for i in range(1, len(x)+1):
  for j in range(1, len(y)+1):
   if x[i-1] == y[j-1]:
    s[i][j] = s[i-1][j-1]
   else:
    s[i][j] = min(costx+s[i-1][j], costy+s[i][j-1])
 
 return s[len(x)][len(y)]


x, y = raw_input().split(' ')
cost = raw_input().split(' ')
cost = map(int , cost)
print "min_cost:{}".format(min_cost(x,y, cost[0], cost[1])) 


