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


it = iter(lines)
reg = {'A': -1, 'B': -1, 'C': -1}
reg['A'], reg['B'], reg['C'] = [nums(next(it)) for _ in range(3)]
program = nums(lines[-1])
INC = 2
out_ = []


def handle_op(op):
    if op<=3: return op
    elif op == 4: return reg["A"]
    elif op == 5: return reg['B']
    elif op == 6: return reg['C']
    elif op == 7: raise ValueError
    raise NotImplementedError


def adv(op): nop = handle_op(op); reg['A'] = reg['A'] // (2**nop)
def bxl(op): reg['B'] = reg['B'] ^ op
def bst(op): op = handle_op(op); reg['B'] = op % 8
def jnz(op): return op
def bxc(op): reg['B'] = reg['B'] ^ reg['C']
def out(op): op = handle_op(op); out_.append(f'{op%8}')
def bdv(op): nop = handle_op(op); reg['B'] = reg['A'] // (2**nop)
def cdv(op): nop = handle_op(op); reg['C'] = reg['A'] // (2**nop)

opcode_to_func = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def run_progam(prog):
    i = 0
    while i < len(prog):
        opcode = prog[i]
        operand = prog[i + 1]

        if opcode == 3 and reg['A'] == 0:
            i += INC
            continue

        if opcode == 3 and reg['A'] != 0:
            x = opcode_to_func[opcode](operand)
            i = x
            continue
        opcode_to_func[opcode](operand)
        i += INC
    return out_


assert isinstance(program, list)

run_progam(program)
print(",".join(out_))

