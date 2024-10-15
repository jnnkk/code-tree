N = float(input())

N_int = int(N // 1)
N_float = N % 1

binary = []
while N_int != 1:
    binary.append(N_int % 2)
    N_int = N_int // 2
binary.append(1)

binary_float = []
while len(binary_float) < 5 and N_float != 0.0:
    N_float *= 2
    binary_float.append(int(N_float // 1))
    N_float %= 1

for i in range(4):
    binary_float.append(0)

for i in binary[::-1]:
    print(i, end='')
print('.',end='')
for i in range(4):
    print(binary_float[i], end='')