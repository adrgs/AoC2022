def update(H, T):
    dist = abs(H[0] - T[0]) + abs(H[1] - T[1])
    if dist <= 1 or (dist == 2 and H[0] != T[0] and H[1] != T[1]):
        # the two heads are touching
        return
    else:
        # the two heads are not touching
        # move the tail
        if H[0] - T[0] == 0:
            # horizontal
            if H[1] - T[1] > 0:
                # right
                T[0], T[1] = (T[0], T[1] + 1)
            else:
                # left
                T[0], T[1] = (T[0], T[1] - 1)
        elif H[1] - T[1] == 0:
            # vertical
            if H[0] - T[0] > 0:
                # up
                T[0], T[1] = (T[0] + 1, T[1])
            else:
                # down
                T[0], T[1] = (T[0] - 1, T[1])
        else:
            # move diagonally
            if H[0] - T[0] > 0:
                # up
                if H[1] - T[1] > 0:
                    # right
                    T[0], T[1] = (T[0] + 1, T[1] + 1)
                else:
                    # left
                    T[0], T[1] = (T[0] + 1, T[1] - 1)
            else:
                # down
                if H[1] - T[1] > 0:
                    # right
                    T[0], T[1] = (T[0] - 1, T[1] + 1)
                else:
                    # left
                    T[0], T[1] = (T[0] - 1, T[1] - 1)

def solve(lines):
    ans = set()
    directions = {
        'U': (1, 0),
        'D': (-1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }
    ROPE_LEN = 10
    rope = [[0, 0] for _ in range(ROPE_LEN)]
    ans.add(tuple(rope[-1]))
    for line in lines:
        line = line.strip()
        if line:
            line = line.split(' ')
            direction, times = line[0], int(line[1])
            for _ in range(times):
                rope[0][0], rope[0][1] = (rope[0][0] + directions[direction][0], rope[0][1] + directions[direction][1])
                
                for i in range(1, ROPE_LEN):
                    update(rope[i-1], rope[i])
                ans.add(tuple(rope[-1]))
    
    print(len(ans))

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()