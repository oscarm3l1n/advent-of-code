import sys
import math
import re


def nums(s):
    x = [int(x) for x in re.findall(r'\d+', s)]
    if len(x) == 1:
        return x[0]
    if isinstance(x, list):
        return x
    raise NotImplementedError


with open(sys.argv[1], 'r') as f:
    D = f.read().strip()
lines = D.split('\n')

DEBUG = False


# DEBUG = True
class DebugDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value) -> None:
        if DEBUG:
            print(f'Setting register {key} = {value}')
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if DEBUG:
            print(f'Getting register {key=} = {super().__getitem__(key)}')
        return super().__getitem__(key)


it = iter(lines)
reg = DebugDict({'A': -1, 'B': -1, 'C': -1})
reg['A'], reg['B'], reg['C'] = [nums(next(it)) for _ in range(3)]
prog = nums(lines[-1])
INC = 2


# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.
def handle_op(op):
    if op <= 3:
        return op
    elif op == 4:
        return reg['A']
    elif op == 5:
        return reg['B']
    elif op == 6:
        return reg['C']
    elif op == 7:
        raise ValueError
    raise NotImplementedError


out_ = []


def exit_program():
    print(','.join(out_))
    exit()


# (opcode 0)
# adv instruction performs division. The numerator is the value in
# the A register. The denominator is found by raising 2 to the power of the
# instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2);
# an operand of 5 would divide A by 2^B.) The result of the division operation
# is truncated to an integer and then written to the A register.
def adv(op):
    nop = handle_op(op)
    reg['A'] = reg['A'] // (2**nop)


# (opcode 1)
# The bxl instruction calculates the bitwise XOR of register B and
# the instruction's literal operand, then stores the result in register B.
def bxl(op):
    reg['B'] = reg['B'] ^ op


# (opcode 2)
# The bst instruction calculates the value of its combo operand
# modulo 8 (thereby keeping only its lowest 3 bits), then writes that value
# to the B register.
def bst(op):
    op = handle_op(op)
    reg['B'] = op % 8


# (opcode 3)
# The jnz instruction does nothing if the A register is 0.
# However, if the A register is not zero, it jumps by setting the instruction
# pointer to the value of its literal operand; if this instruction jumps,
# the instruction pointer is not increased by 2 after this instruction.
def jnz(op):
    if reg['A'] == 0:
        print(out_)
        raise ValueError
        # exit_program()
    return op


# (opcode 4)
# The bxc instruction calculates the bitwise XOR of register B and
# register C, then stores the result in register B. (For legacy reasons,
# this instruction reads an operand but ignores it.)
def bxc(op):
    reg['B'] = reg['B'] ^ reg['C']


# (opcode 5)
# The out instruction calculates the value of its combo operand
# modulo 8, then outputs that value. (If a program outputs multiple values,
# they are separated by commas.)
def out(op):
    op = handle_op(op)
    print('adding to out_', op % 8)
    out_.append(f'{op%8}')


# (opcode 6)
# The bdv instruction  works exactly like the adv instruction except
# that the result is stored in the B register. (The numerator is still read
# from the A register.)
def bdv(op):
    nop = handle_op(op)
    reg['B'] = reg['A'] // (2**nop)


# (opcode 7)
# The cdv instruction  works exactly like the adv instruction except
# that the result is stored in the C register. (The numerator is still read
# from the A register.)
def cdv(op):
    nop = handle_op(op)
    reg['C'] = reg['A'] // (2**nop)


opcode_to_func = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def run_assertions():
    global out_
    reg['C'] = 9
    opcode_to_func[2](6)
    assert reg['B'] == 1

    reg['A'] = 10
    out_ = []
    opcode_to_func[5](0)
    opcode_to_func[5](1)
    opcode_to_func[5](4)
    assert out_ == ['0', '1', '2']

    print('-' * 30)
    reg['A'] = 2024
    out_ = []
    opcode_to_func[0](1)
    opcode_to_func[5](4)
    opcode_to_func[3](0)
    prog = [0, 1, 5, 4, 3, 0]
    i = 0
    while i < len(prog):
        opcode = prog[i]
        operand = prog[i + 1]
        if opcode == 3 and reg['A'] == 0:
            i += INC
            continue
        if opcode == 3:
            x = opcode_to_func[opcode](operand)
            i = x
            continue
        opcode_to_func[opcode](operand)
        i += INC
    assert out_ == [str(x) for x in [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]], f'actual {out_}'
    assert reg['A'] == 0

    reg['B'] = 29
    opcode_to_func[1](7)
    assert reg['B'] == 26

    print('-' * 30)
    reg['B'] = 2024
    reg['C'] = 43690
    opcode_to_func[4](0)
    assert reg['B'] == 44354


# run_assertions()

assert isinstance(prog, list)

i = 0
while i < len(prog):
    opcode = prog[i]
    operand = prog[i + 1]

    print(f'{opcode=} {operand=}')
    print(prog)
    print(' ' * 3 * i, '^')

    if opcode == 3 and reg['A'] == 0:
        i += INC
        continue

    if opcode == 3 and reg['A'] != 0:
        x = opcode_to_func[opcode](operand)
        i = x
        if DEBUG:
            input()
        continue
    opcode_to_func[opcode](operand)
    if DEBUG:
        input()
    i += INC


exit_program()
