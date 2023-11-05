arr = [
    ['a', 2, 100], 
    ['b', 2, 20], 
    ['c', 1, 40], 
    ['d', 3, 35], 
    ['e', 1, 25]
    ]
print("Following is maximum profit sequence of Jobs: ")
# length of array
n = len(arr)
t = 3
# Sort all jobs according to
# decreasing order of profit
for i in range(n):
   for j in range(n - 1 - i):
     if arr[j][2] < arr[j + 1][2]:
       arr[j], arr[j + 1] = arr[j + 1], arr[j]

# To keep track of free time slots
result = [False] * t

# To store result (Sequence of jobs)
job = ['-1'] * t

# Iterate through all given jobs
for i in range(len(arr)):

   # Find a free slot for this job
   # (Note that we start from the
   # last possible slot)
   for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

     # Free slot found
     if result[j] is False:
       result[j] = True
       job[j] = arr[i][0]
       break

# print the sequence
print(job)