input_ = open('input8.txt').read().splitlines();

def initialize_variable(variable, array_variable):
    if not variable in array_variable:
        array_variable[variable] = 0


def part1():
    array_variables= {}

    max_temp = 0

    ops = {'>': (lambda x, y: x > y),
           '<': (lambda x, y: x < y),
           '>=': (lambda x, y: x >= y),
           '<=': (lambda x, y: x <= y),
           '==': (lambda x, y: x == y),
           '!=': (lambda x, y: x != y),
           'inc': (lambda x, y: x + y),
           'dec': (lambda x, y: x - y)}

    for line in input_:

        variable, operation, value, _, variable_in_term, term, value_in_term = line.split()

        initialize_variable(variable, array_variables)
        initialize_variable(variable_in_term, array_variables)

        if ops[term](array_variables[variable_in_term], int(value_in_term)):
            array_variables[variable] = ops[operation](array_variables[variable],int(value))

        max_value_variable = array_variables[max(array_variables,key=array_variables.get)]
        if max_temp < max_value_variable:
            max_temp = max_value_variable


    print(array_variables[max(array_variables,key=array_variables.get)])
    print(max_temp)


part1()