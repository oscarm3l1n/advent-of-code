import sys

with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

def get_number_and_color(bag):
    numbers_and_colors = bag.split(",")
    numbers = []
    colors = []
    for item in numbers_and_colors:
        number, color = "", None
        print(item)
        for i, ch in enumerate(item):
            if ch.isdigit():
                number += ch
            else:
                color = item[i:]
                break
        numbers.append(int(number))
        colors.append(color)
    
    return [(c, n) for c, n in zip(colors, numbers)]

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14
limits = {
    "blue": BLUE_CUBES,
    "red": RED_CUBES,
    "green": GREEN_CUBES
}

def p1():
    game = 1
    indexes = []
    for line in data:
        line = line[len(f"Game {game}: "):]
        bags = line.replace(" ", "").split(";")
        possible = True
        for bag in bags:
            pairs = get_number_and_color(bag)
            for color, number in pairs:
                if number > limits[color]:
                    possible = False
                    break
        indexes.append(game if possible else 0)
        game += 1
    print("part 1:", sum(indexes))

def p2():
    game = 1
    result = 0
    for line in data:
        line = line[len(f"game {game}: "):]
        bags = line.replace(" ", "").split(";")
        game_results = []
        for bag in bags:
            pairs = get_number_and_color(bag)
            for pair in pairs:
                game_results.append(pair)
        colors = {
            "red": float("-inf"),
            "blue": float("-inf"),
            "green": float("-inf")
        }
        for color, number in game_results:
            colors[color] = max(colors[color], number)
        
        tmp = 1
        for color, number in colors.items():
            tmp *= number
        result += tmp
        game += 1
    print("part 2:", result)

p1()
p2()