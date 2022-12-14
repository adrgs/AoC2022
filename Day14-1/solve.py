def solve(lines):
    grid = [['.' for _ in range(1024)] for __ in range(1024)]

    for line in lines:
        line = line.strip()
        if line:
            nodes = [(int(node.split(',')[0]), int(node.split(',')[1])) for node in line.split(' -> ')]
            
            for i in range(1, len(nodes)):
                if nodes[i][0] == nodes[i-1][0]:
                    for j in range(min(nodes[i][1], nodes[i-1][1]), max(nodes[i][1], nodes[i-1][1])+1):
                        grid[j][nodes[i][0]] = '#'
                else:
                    for j in range(min(nodes[i][0], nodes[i-1][0]), max(nodes[i][0], nodes[i-1][0])+1):
                        grid[nodes[i][1]][j] = '#'

    grid[0][500] = '+'

    count = 0

    while True:
        count += 1
        sand = (1, 500)
        abyss = False

        grid[sand[0]][sand[1]] = 'o'

        while grid[sand[0]+1][sand[1]] == '.' or grid[sand[0]+1][sand[1]+1] == '.' or grid[sand[0]+1][sand[1]-1] == '.':
            grid[sand[0]][sand[1]] = '.'
            if grid[sand[0]+1][sand[1]] == '.':
                sand = (sand[0]+1, sand[1])
            elif grid[sand[0]+1][sand[1]-1] == '.':
                sand = (sand[0]+1, sand[1]-1)
            elif grid[sand[0]+1][sand[1]+1] == '.':
                sand = (sand[0]+1, sand[1]+1)
            
            grid[sand[0]][sand[1]] = 'o'

            if sand[0] >= len(grid)-1 or sand[1] >= len(grid[0])-1 or sand[0] <= 1 or sand[1] <= 1:
                count -= 1
                abyss = True
                break

        if abyss:
            break
    
    print(count)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()