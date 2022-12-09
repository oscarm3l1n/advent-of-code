

def solution(n_knots):
    knots = [(0, 0) for _ in range(n_knots)]
    
    visited = set()
    visited.add(knots[-1])

    print(len(visited))



solution(2)