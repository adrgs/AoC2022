def solve(lines):
    ans = set()
    directions = {
        'U': (1, 0),
        'D': (-1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }
    H = (0, 0)
    T = (0, 0)
    ans.add(T)
    for line in lines:
        line = line.strip()
        if line:
            line = line.split(' ')
            direction, times = line[0], int(line[1])
            for _ in range(times):
                H = (H[0] + directions[direction][0], H[1] + directions[direction][1])
                
                dist = abs(H[0] - T[0]) + abs(H[1] - T[1])
                if dist <= 1 or (dist == 2 and H[0] != T[0] and H[1] != T[1]):
                    # the two heads are touching
                    continue
                else:
                    # the two heads are not touching
                    # move the tail
                    if H[0] - T[0] == 0:
                        # horizontal
                        if H[1] - T[1] > 0:
                            # right
                            T = (T[0], T[1] + 1)
                        else:
                            # left
                            T = (T[0], T[1] - 1)
                    elif H[1] - T[1] == 0:
                        # vertical
                        if H[0] - T[0] > 0:
                            # up
                            T = (T[0] + 1, T[1])
                        else:
                            # down
                            T = (T[0] - 1, T[1])
                    else:
                        # move diagonally
                        if H[0] - T[0] > 0:
                            # up
                            if H[1] - T[1] > 0:
                                # right
                                T = (T[0] + 1, T[1] + 1)
                            else:
                                # left
                                T = (T[0] + 1, T[1] - 1)
                        else:
                            # down
                            if H[1] - T[1] > 0:
                                # right
                                T = (T[0] - 1, T[1] + 1)
                            else:
                                # left
                                T = (T[0] - 1, T[1] - 1)
                ans.add(T)
    
    print(len(ans))

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()