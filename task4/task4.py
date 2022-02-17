nums = list()
file = str(input())
alg_mean = 0
summa = 0
min_count_step = 0

with open(file, 'r') as inf:
    for line in inf:
        nums.append(line.rstrip())
        nums = [int(i) for i in nums]
        
for i in nums:
    summa += i
alg_mean = summa // len(nums)

for i in nums:
    min_count_step += abs(i - alg_mean)
print(min_count_step)