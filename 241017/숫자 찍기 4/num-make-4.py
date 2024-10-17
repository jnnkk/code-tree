import sys

N = int(sys.stdin.readline().strip())

def solve(N):

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    direction = 'r'
    x, y = 0, 0

    for i in range(1, N**2+1):
        matrix[x][y] = i
        
        if direction == 'r':
            if 0 <= y+1 < N:
                if matrix[x][y+1] == 0:
                    y += 1
                else:
                    direction = 'd'
                    x += 1
            else:
                direction = 'd'
                x += 1
        elif direction == 'd':
            if 0 <= x+1 < N:
                if matrix[x+1][y] == 0:
                    x += 1
                else:
                    direction = 'l'
                    y -= 1
            else:
                direction = 'l'
                y -= 1
        elif direction ==  'l':
            if 0 <= y-1 < N:
                if matrix[x][y-1] == 0:
                    y -= 1
                else:
                    direction = 'u'
                    x -= 1
            else:
                direction = 'u'
                x -= 1
        elif direction == 'u':
            if 0 <= x-1 < N:
                if matrix[x-1][y] == 0:
                    x -= 1
                else:
                    direction = 'r'
                    y += 1
            else:
                direction = 'y'
                y += 1

    return matrix

result = solve(N)

for r in result:
    print(*r)