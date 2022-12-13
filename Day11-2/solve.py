import re

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.inspects = 0

    def add_op(self, op):
        self.op = op

    def add_test(self, test):
        self.test = test

    def add_div(self, div):
        self.div = div

    def add_pass_true(self, id_monkey):
        self.pass_true = id_monkey

    def add_pass_false(self, id_monkey):
        self.pass_false = id_monkey

    def round(self, Monkeys):
        # print(f'\nMonkey {self.id}: ')
        should_rerun = False
        for i in range(len(self.items)):
            # print(f'Monkey inspects an item with a worry level of {self.items[i]}')
            self.inspects += 1
            self.items[i] = self.div(self.items[i])
            self.items[i] = self.op(self.items[i])
            # print(f'Worry level is {self.items[i]}')
            # print(f'Worry level is divided by 3 to {self.items[i]}')
            if self.test(self.items[i]):
                # print(f'Item with worry level {self.items[i]} is thrown to monkey {self.pass_true}')
                Monkeys[self.pass_true].items.append(self.items[i])
                should_rerun = True
                del self.items[i]
                break
            else:
                # print(f'Item with worry level {self.items[i]} is thrown to monkey {self.pass_false}')
                Monkeys[self.pass_false].items.append(self.items[i])
                should_rerun = True
                del self.items[i]
                break
        if should_rerun:
            self.round(Monkeys)
        

def solve(lines):
    Monkeys = []

    r1 = r'Monkey (\d+):'
    r2 = r'Starting items: (.*)'
    r3 = r'Operation: new = (.*)'
    r4 = r'Test: divisible by (\d+)'
    r5 = r'If true: throw to monkey (\d+)'
    r6 = r'If false: throw to monkey (\d+)'

    divisor = 1

    for line in lines:
        line = line.strip()
        if line:
            res1 = re.match(r1, line)
            if res1:
                Monkeys.append(Monkey(int(res1.group(1))))
            res2 = re.match(r2, line)
            if res2:
                Monkeys[-1].items = [int(x) for x in res2.group(1).split(', ')]
            res3 = re.match(r3, line)
            if res3:
                a = eval('lambda old: ' + res3.group(1))
                Monkeys[-1].add_op(a)
            res4 = re.match(r4, line)
            if res4:
                nr = int(res4.group(1))
                divisor *= nr
                Monkeys[-1].add_test(eval(f'lambda x: x % {nr} == 0'))
            res5 = re.match(r5, line)
            if res5:
                Monkeys[-1].add_pass_true(int(res5.group(1)))
            res6 = re.match(r6, line)
            if res6:
                Monkeys[-1].add_pass_false(int(res6.group(1)))

    for monkey in Monkeys:
        monkey.add_div(eval(f'lambda x: x % {divisor}'))

    for round in range(10000):
        if round%1000 == 0:
            print(round)
        for monkey in Monkeys:
            monkey.round(Monkeys)

    monkey_business = []
    for monkey in Monkeys:
        print('Monkey', monkey.id, 'inspected', monkey.inspects, 'items')
        monkey_business.append(monkey.inspects)

    monkey_business.sort(reverse=True)
    print(monkey_business[0] * monkey_business[1])

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()