from pathlib import Path

def found(pathArr, startPoint, finPoint):
    y, x = startPoint
    pathArr[y][x] = 1
    weight = 1
    for _ in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:

                    # Вверх
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1

                    # Вниз
                    if y < len(pathArr) - 1 and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1

                    # Влево
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1

                    # Вправо
                    if x < len(pathArr[y]) - 1 and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1

                    # Конечная точка
                    if (y, x) == finPoint:
                        return True

        weight += 1
    return False

def printPath(pathArr, finPoint):
    y, x = finPoint
    weight = pathArr[y][x]
    result = []

    while weight > 1:
        weight -= 1

        if y > 0 and pathArr[y - 1][x] == weight:
            result.append('Вверх')
            y -= 1

        elif y < len(pathArr) - 1 and pathArr[y + 1][x] == weight:
            result.append('Вниз')
            y += 1

        elif x > 0 and pathArr[y][x - 1] == weight:
            result.append('Влево')
            x -= 1

        elif x < len(pathArr[y]) - 1 and pathArr[y][x + 1] == weight:
            result.append('Вправо')
            x += 1
    result.reverse()
    return result


WALL = -1
FREE = 0
START = 1

labyrinth = []
pozIn = pozOut = None

file_path = Path(__file__).parent / "labyrinth.txt"
with open(file_path, encoding="utf-8") as f:
    for line in f:
        row = []
        for cell in line.strip().split():
            if cell  == "1":
                row.append(WALL)
            elif cell == "A":
                row.append(START)
                pozIn = (len(labyrinth), len(row) - 1)
            elif cell == "B":
                row.append(FREE)
                pozOut = (len(labyrinth), len(row) - 1)
            else:
                row.append(FREE)
        labyrinth.append(row)
print(labyrinth)

if pozIn is None or pozOut is None:
    raise ValueError("В лабиринте должен быть вход A и выход B")

found_path = found(labyrinth, pozIn, pozOut)

if not found_path:
    print("Путь не найден!")
else:
    path = printPath(labyrinth, pozOut)
    print("Лабиринт с волнами:")

    for row in labyrinth:
        print(" ".join(f"{cell:^3}" for cell in row))

    print("\nПуть:")
    print(path)