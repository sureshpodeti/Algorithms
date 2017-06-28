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
'''
def min_cost(x,y, i, j , costx, costy):
 if i<0 and j<0:
  return 0

 if i<0:
  return costy*(j+1)

 if j<0:
  return costx*(i+1)

 if x[i] == y[j]:
  return min_cost(x,y, i-1, j-1, costx, costy)

 return min(costx+ min_cost(x, y, i-1, j, costx, costy), costy+min_cost(x,y, i, j-1, costx, costy))


x, y = raw_input().split(' ')
cost = raw_input().split(' ')
cost = map(int , cost)
print "min_cost:{}".format(min_cost(x,y, len(x)-1, len(y)-1,  cost[0], cost[1])) 


