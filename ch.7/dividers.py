import math

num = int(input())

sum = 0

for i in range(1, num + 1):
    sum += math.factorial(i)

print(sum)