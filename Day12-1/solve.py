def solve(lines):
    grid = []

    i = 0

    for line in lines:
        line = line.strip()
        if line:
            grid.append(list(line))
            try:
                j = line.index('S')
                start = (i, j)
            except ValueError:
                pass
            try:
                j = line.index('E')
                end = (i, j)
            except ValueError:
                pass
        i += 1
        
    visited = set()

    grid[start[0]][start[1]] = 'a'
    grid[end[0]][end[1]] = 'z'

    def get_dist(pos):
        # return manhattan distance between pos and end
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    MIN_STEPS = float("inf")

    queue = [(start, 0)]
    visited = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
    visited[start[0]][start[1]] = 1
    while queue:
        pos, steps = queue.pop(0)

        if steps >= MIN_STEPS:
            continue

        if pos == end:
            print(steps)

        i, j = pos
        if i > 0 and ord(grid[i][j]) + 1 >= ord(grid[i-1][j]) and visited[i-1][j] == 0:
            visited[i-1][j] = 1
            queue.append(((i-1, j), steps+1))
        if i < len(grid)-1 and ord(grid[i][j]) + 1 >= ord(grid[i+1][j]) and visited[i+1][j] == 0:
            visited[i+1][j] = 1
            queue.append(((i+1, j), steps+1))
        if j > 0 and ord(grid[i][j]) + 1 >= ord(grid[i][j-1]) and visited[i][j-1] == 0:
            visited[i][j-1] = 1
            queue.append(((i, j-1), steps+1))
        if j < len(grid[0])-1 and ord(grid[i][j]) +1 >= ord(grid[i][j+1]) and visited[i][j+1] == 0:
            visited[i][j+1] = 1
            queue.append(((i, j+1), steps+1))


def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()