import re
input_ = open('input9.txt').read().splitlines();

for line in input_:
    line = re.sub('!.', '', line)
    length_line = len(line)
    line = re.sub('<[^>]*>','<>',line)
    length_garbage = length_line - len(line)
    line = re.sub('<>','',line)
    line = re.sub('[^{}]','',line)
    result = 0
    weight = 0
    for i in line:
        if i == '{':
            weight += 1
        else:
            result += weight
            weight -= 1

    print(result)
    print(length_garbage)