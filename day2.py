from enum import Enum


class Directions(str, Enum):
    FORWARD = 'forward'
    UP = 'up'
    DOWN = 'down'


def navigate(controls: list[tuple[str, int]]) -> list:
    cords = [0, 0]
    for command, value in controls:
        match command:
            case Directions.FORWARD:
                cords[0] += value
            case Directions.UP:
                cords[1] -= value
            case Directions.DOWN:
                cords[1] += value
    return cords


def aim(controls: list[tuple[str, int]]) -> tuple:
    aim = 0
    x, y = 0, 0
    for command, value in controls:
        match command:
            case Directions.FORWARD:
                x += value
                y += aim * value if aim != 0 else y
            case Directions.UP:
                aim -= value
            case Directions.DOWN:
                aim += value
    return (x, y)
        

with open('d2data.txt') as f:
    data = f.readlines()
    controls = map((lambda comm: (comm[0], int(comm[1]))), [i.split() for i in data])

print(aim(controls))
print(navigate(controls))
