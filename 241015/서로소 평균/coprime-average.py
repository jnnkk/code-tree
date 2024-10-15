import math
import sys


n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())

count = 0
num_sum = 0

for i in a:
    if math.gcd(i, x) == 1:
        count += 1
        num_sum += i

print('{:.2f}'.format(num_sum / count))