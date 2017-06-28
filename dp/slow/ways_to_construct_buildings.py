'''
  Count possible ways to construct buildings:
   Given an input number 'n' of sections and each section has 2 plots on either 
   side of the road. Find all possible ways to construct buildings in the plots
   such that there is a space between any 2 buildings.

   description:
    n = 1
         -----
        |  A  |
        -------
 -----------------------
          ROAD
 ------------------------
        -----
       |  B  |
       -------

  A,B are the plots. we can consider only one side and count the no.of ways
  we can construct and square that to get the total number.

  In one side, solutions are: {S, B} = 2 , S = Space, B = building
  so, 2*2 = 4 is the answer
  
  brute-force solution:
   Let f(n) denote the total #of ways to construct
   
   f(n) = #ways to construct if we construct building at nth plot +
          #wasy to construct if we leave space at nth plot

   f(n) = f(n-1) + f(n-2)   # it is fibonacci series

   base cases:
      if n == 1 then 
           return 2
      if n == 0 then 
           return 1

   time complexicity: O(2^n)
'''

def construct(n):
 if n == 0:
  return 1

 if n == 1:
  return 2

 return construct(n-1) + construct(n-2)



n = int(raw_input())
print "#of_ways:{}".format(construct(n)**2)
