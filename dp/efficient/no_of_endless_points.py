# _*_ coding:utf-8 _*_
'''
 
Find number of endless points

Given a binary N x N matrix, we need to find the total number of matrix positions from which there is an endless path. Any position (i, j) is said to have an endless path if and only if all of the next positions in its row(i) and its column(j) should have value 1. If any position next to (i,j) either in row(i) or in column(j) will have 0 then position (i,j) doesn’t have any endless path.

dynamic programming approach:
 create two matrix for accounting for row and column  

time complexicity: O(n^2)
space complexicity: O(n^2)
'''

import sys
def endless_points(m, n):
 row = [[ 0 for i in range(n+1)] for x in range(n)]
 column = [[ 0 for i in range(n)] for x in range(n+1)]
 
 # intialize row matrix
 for i in range(0,n):
  row[i][n] = 1
 
 # intialize column matrix
 for i in range(0, n):
  column[n][i] = 1

 # construct row matrix
 for i in range(n-1, -1, -1):
  for j in range(n-1, -1, -1):
   if m[i][j] == 1:
    row[i][j] = row[i][j+1]
   else:
    row[i][j] = 0

 # construct column matrix
 for i in range(n-1, -1,-1):
  for j in range(n-1, -1, -1):
   if m[i][j] == 1:
     column[i][j] = column[i+1][j]
   else:
     column[i][j] = 0

 #counting the no.of end points 
 count = 0
 for i in range(0, n):
  for j in range(0,n): 
   count += min(row[i][j], column[i][j])

 return count
m = [[1,0,1, 1],[0, 1,1,1], [1,1,1,1], [0,1,1,0]]
print "endless_points:{}".format(endless_points(m, len(m)))
