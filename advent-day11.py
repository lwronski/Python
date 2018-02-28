import re
input_ = open('input11.txt').read().split(',');

ops = {'s': (lambda y, x: (y-1,x)),
           'n': (lambda y, x: (y+1,x)),
           'nw': (lambda y, x: (y+1,x-1)),
           'se': (lambda y, x: (y-1,x+1)),
           'sw': (lambda y, x: (y,x-1)),
           'ne': (lambda y, x: (y,x+1))}


def deletewhiespace(direction):
    return re.sub('\n','',direction)

def count_step_away(y,x):
    if ( x >= 0 and y >= 0 ) or ( x < 0 and y < 0 ):
        return abs(x) + abs(y)
    else:
        return min ( abs(x), abs(y) ) + abs( abs(x) - abs(y))

def part1():

    global ops
    x,y = 0,0
    result = -1

    for direction in input_:
        direction = deletewhiespace(direction)
        y,x = ops[direction](y,x)
        print(y,x)
        result = max(result,count_step_away(y,x))

    print(count_step_away(y,x))
    print(result)




part1()