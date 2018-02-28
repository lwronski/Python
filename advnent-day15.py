input_ = open('input15.txt').read().split()


def genA(A_number):
    return (A_number*16807)%2147483647


def genB(B_number):
    return (B_number*48271)%2147483647


def upper_bit(x):
    while x & (x - 1):
        x &= x - 1
    return x

def part1(A_number, B_number):

    counter = 0
    for i in range(40000000):
        A_number = genA(A_number)
        B_number = genB(B_number)
        if A_number & 0xFFFF == B_number & 0xFFFF:
            counter += 1

    return counter

def part2(A_number, B_number):

    counter = 0
    for i in range(500000):
        while A_number % 4 != 0:
            A_number = genA(A_number)
        while B_number % 8 != 0:
            B_number = genB(B_number)
            counter += 1
        A_number = genA(A_number)
        B_number = genB(B_number)

    return counter



# part1(int(input_[0]), int(input_[1]))
part2(int(input_[0]), int(input_[1]))