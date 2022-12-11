with open('input.in') as f:
    data = f.read().split('\n\n')


class Monkey:
    def __init__(self, operation, divisible, false, true, id):
        self.items = []
        self.operation = operation
        self.divisible = divisible
        self.false = false
        self.true = true
        self.count = 0
        self.id = id
    
    def add_item(self, item):
        self.items.append(item)


def solve(n, is_part1=False):
    monkeys = []

    # init monkeys
    for d in data:
        lines = d.split('\n')
        items = lines[1].split()
        items = [int(i.replace(',','')) for i in items[2:]]
        operation = lines[2].split('new = ')[-1]

        divisible = int(lines[3].split()[-1])

        if_true = lines[4].split()[-1]
        if_false = lines[5].split()[-1]

        m = Monkey(operation, divisible, if_false, if_true, id=len(monkeys))
        for item in items:
            m.add_item(item)

        monkeys.append(m)

    # for part 2
    modulus = 1
    for m in monkeys:
        modulus *= m.divisible

    for _ in range(n):
        for i in range(len(monkeys)):
            for _ in range(len(monkeys[i].items)):
                monkeys[i].count += 1
                item = monkeys[i].items.pop()
                if not is_part1:
                    item = item % modulus
                #print('\nCurrent item', item)
                #print(f'\tMonkey inspects an item with a worry level of {item}')
                formula = monkeys[i].operation.replace('old', str(item))
                res = eval(formula)
                #print(f'\tWorry level is changed from {item} to {res}')
                
                if is_part1:
                    res = res // 3

                cond = False
                if res % monkeys[i].divisible == 0:
                    cond = True
                
                to_monkey = -1

                if cond:
                    to_monkey = int(monkeys[i].true)
                    #print(f'\tCurrent worry level is NOT divisible by {monkeys[i].divisible}')
                else:
                    to_monkey = int(monkeys[i].false)
                    #print(f'\tCurrent worry level is divisible by {monkeys[i].divisible}')

                
                #print(f'\tItem with worry level {res} is thrown to to_monkey {to_monkey}')
                monkeys[to_monkey].add_item(res)
        
    
    counts = [m.count for m in monkeys]
    counts = sorted(counts)
    print("Counts:", counts)
    return counts[-1] * counts[-2]


if __name__ == '__main__':
    print(f'Part 1: {solve(20, True)}')
    print(f'Part 2: {solve(10000, False)}')