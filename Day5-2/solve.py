import re

def parse_stacks(lines):
    r = re.compile(r'\[([A-Z])\]')
    stacks = lines[-1].split()
    stacks = [[] for _ in range(len(stacks))]
    for line in lines[:-1]:
        if line:
            for match in r.finditer(line):
                stacks[match.start()//4].append(match.group(1))
    for stack in stacks:
        stack.reverse()
    return stacks

def move(n, src, dest):
    dest.extend(src[-n:])
    del src[-n:]

def solve(lines):
    ans = []
    stacks, instructions = lines[:lines.index('\n')], lines[lines.index('\n')+1:]
    stacks = parse_stacks(stacks)
    
    for instruction in instructions:
        instruction = instruction.strip()
        if instruction:
            instruction = instruction.split()
            n, src, dest = int(instruction[1]), stacks[int(instruction[3])-1], stacks[int(instruction[5])-1]
            move(n, src, dest)

    for stack in stacks:
        ans.append(stack[-1])

    print(''.join(ans))

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()