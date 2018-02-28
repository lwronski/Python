import re
from queue import *

input_ = open('input12.txt').read().splitlines();

def get_parent(line):
    return re.search('(\d+)',line).group(1)

def get_child(line):
    pattern = re.compile('(?!\d+ <)(\d+)')
    return re.findall(pattern,line)


def dfs(nodes, start_node, flags):

    flags[start_node] = True

    q = Queue()
    q.put(start_node)

    while not q.empty():
        front = q.get()
        for i in nodes[front]:
            if not i in flags:
                q.put(i)
                flags[i] = True

    return len(flags)

def part1():

    nodes = {}
    flags = {}

    for line in input_:

        parent = get_parent(line)
        nodes[parent] = []
        for i in get_child(line):
            nodes[parent].append(i)

    print(dfs(nodes,str(0), flags))

    flags = {}
    counter = 0

    for i in nodes:
        if not i in flags:
            dfs(nodes,i,flags)
            counter += 1

    print(counter)

part1()