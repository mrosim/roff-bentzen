def sub_matrix_sumi(input_matrix):
    sum_element = [sum([int(r) for r in i]) for i in input_matrix]
    return sum_element


def sub_matrix_sumf(input_matrix):
    sum_element = [sum([float(r) for r in i]) for i in input_matrix]
    return sum_element


def transpose(input_matrix):
    tsp_matrix = [[input_matrix[x][i] for x, n in enumerate(input_matrix)] for i, n in
                  enumerate(input_matrix[0])]
    return tsp_matrix


