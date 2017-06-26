'''
 Weighted job scheduling:
  Given N jobs where every job is represented by following three elements of it.

    Start Time
    Finish Time
    Profit or Value Associated

Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

Example:

Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50} 
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}

       A            B              	C
   +--------+  +------------+ +-------------------+ 
   1        2  3            5 6                   19
                                             D
            +----------------------------------------------------------------+
            2                                                                100

   possible solutions are:
          solutions = {A+B+C, A+C}
         1. A+B+C = 50+20+100 = 170
         2. A+C   = 50 + 200  = 250 

Output: The maximum profit is 250.

We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3 
but the profit with this schedule is 20+50+100 which is less than 250.

 brute-force solution:
  1. first sortout all the jobs according to their finish time
  2. we can think of total possible solutions as,
      total_no_of_solutions = solutions where nth job included + solutions where nth job not included
  3. Let f(s, f, p, n) denote the maximum profit obtained by scheduling the n jobs
         f(s,f,p,n) =  solutions where nth job included +  f(s, f,p n-1)

  4. Here the tricky part is, calculating the solutions where nth job included:
          we need to figurout the latest job which can be scheduled if nth job is included, and recur same for that job
        
  5. base case: if n == 1 then 
                   return p[n-1] # simply return profit of the first job


'''
def latest_non_conflict_job(s, f, n):
  for i in range(n-1, -1, -1):
   if f[i] <= s[n-1]:
    return i

  return -1

def job_schedule_profit(s, f, p, n):
  # base case
  if n == 1:
   return p[n-1]

  # when it is included
  i = latest_non_conflict_job(s,f,n)
  if not i == -1:
   include_profit = p[n-1] + job_schedule_profit(s, f, p, i+1)
  
  # when it is not included
  exclude_profit = job_schedule_profit(s, f, p, n-1)

  return max(include_profit, exclude_profit)



# for simplicity we have considered already sorted input by finish time 
s = [1, 3, 6, 2]
f = [2, 10, 19, 100]
p = [50, 20, 100, 200]
print "max_job_scheduling_profit:{}".format(job_schedule_profit(s, f, p, len(s)))
