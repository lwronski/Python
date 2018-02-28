import re

input_ = open('input13.txt').read().splitlines();

def get_layer_depth(line):
    pattern = re.search('(\d+): (\d+)',line)

    return int(pattern.group(1)), int(pattern.group(2))


def load_data():
    firewall = {}

    for line in input_:
        layer, depth = get_layer_depth(line)
        firewall[layer] = depth
    return firewall


def part1(firewall, start_delay, check_part2):

    result = 0

    for index_layer in range(int(max(firewall))+1):
        #entry
        if not index_layer in firewall:
            continue
        elif (start_delay + index_layer) % ( firewall[index_layer] * 2 - 2) == 0:
            result += index_layer * firewall[index_layer]
            if check_part2:
                return -1

    return result

firewall = load_data()

print(part1(firewall,0,False))


def part2(firewall):


    delay = 0
    while True:
        # print(part1(firewall,delay), delay)
        if part1(firewall,delay, True) == 0 :
            return delay

        delay += 1

    return delay


print(part2(firewall))