import sys

nums = []
num_set = set()
N = int(sys.stdin.readline().strip())

result = 0

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    nums.append(num)
    num_set.add(num)

def sliding_window(num_list, K):
    left = 0
    right = 0
    k_count = 0
    max_count = 0

    while right < len(num_list):
        if num_list[right] == K:
            k_count += 1
            right += 1
            continue
        if num_list[left] != num_list[right]:
            max_count= max(max_count, right - left - k_count)
            left = right
            k_count = 0
        else:
            right += 1

    max_count= max(max_count, right - left - k_count)

    return max_count

max_result = 0

while num_set:
    k = num_set.pop()
    max_result = max(max_result, sliding_window(nums, k))

print(max_result)