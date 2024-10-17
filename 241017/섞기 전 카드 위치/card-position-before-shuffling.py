import sys

N = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().split()))

L = list(map(int, sys.stdin.readline().split()))

def restore(N, A, L):

    re_A = [0 for _ in range(N)]

    for i in range(N):
        re_A[i] = A.index(i+1)

    for _ in range(3):
        temp = [0 for _ in range(N)]
        for j in range(N):
            temp[re_A[j]] = L[j]
        L = temp

    return L


for ans in restore(N, A, L):
    sys.stdout.write(str(ans) + '\n')