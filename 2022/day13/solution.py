
with open('test.in', 'r') as f:
    data = f.read().split('\n\n')


def check(a, b):
    if isinstance(a) and isinstance(b):
        return check(a, b) # ???

def check_int(a,b):
    return a > b


res = []
correct = 0
wrong = False
for d in data:
    p1, p2 = d.split('\n')

    a1 = eval(p1)
    a2 = eval(p2)

    
    for e1, e2 in zip(a1, a2):
        if isinstance(e1,int) and isinstance(e2,int):
            if check_int(e1,e2):
                wrong = True
        elif isinstance(e1,list) and isinstance(e2,list):
            for a, b in zip(e1, e2):

                if len(a) > len(b):
                    wrong = True

    print(a1)
    print(a2)
    if not wrong:
        print("correct!")
        correct += 1

print(correct)

