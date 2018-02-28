input_ = open('input16.txt').read().split(',');


def rotate(l, n):
    return l[n:] + l[:n]


def move(move, array_date):
    array_date = array_date[-move:] + array_date[:len(array_date) - move]
    return array_date


def exchange(first, second, array_date):
    array_date[first], array_date[second] = array_date[second], array_date[first]
    return array_date


def partner(first_value, second_value, array_data):
    return exchange(array_data.index(first_value), array_data.index(second_value), array_data)


def split_with_backlash(string):
    split_string = string.split("/")
    split_string[0] = split_string[0][1:]
    return split_string


def part1(array_dance):
    for i in input_:
        if i[0] == 's':
            array_dance = move(int(i[1:]), array_dance)
        elif i[0] == 'x':
            split_in = split_with_backlash(i)
            array_dance = exchange(int(split_in[0]), int(split_in[1]), array_dance)
        else:
            array_dance = partner(i[1], i[3], array_dance)

    return array_dance


def array_to_string(array_date):
    output = ""
    for i in array_date:
        output += i
    return  output

def part2(times, array_dance):
    result = []
    for i in range(times):
        array_dance = part1(array_dance)
        if not array_to_string(array_dance) in result:
            result.append(array_to_string(array_dance))
        else:
            return i, array_dance
    return 0, array_dance


def create_array_dance( ):
    array_dance = []
    for i in range(97, 113):
        array_dance.append(chr(i))
    return  array_dance

array_dance = create_array_dance()

#part1
print(array_to_string(part1(array_dance)))


#part2

array_dance = create_array_dance()

cycle, array_dance = part2(1000000000,array_dance)
modulo = 1000000000%cycle
print(modulo)
cycle, array_dance = part2( modulo-1,array_dance)

print(array_to_string(array_dance))

# print( array_to_string(array_dance) )
