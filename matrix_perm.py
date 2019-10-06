from ChiSquare import ChiSquare
import random


class Permutation:
    def __init__(self, input_matrix):
        self.input_matrix = input_matrix

    def perm(self):
        # call the class chi-square for the observed matrix
        tc = ChiSquare(self.input_matrix)

        # column-sum and line-sum and chi-square value
        sum_cln = tc.sum_column()
        sum_ln = tc.sum_line()
        ### x = tc.chi_square_tot()
        ### print(x)

        # produce a list of random number as long as the total sum of the observed matrix
        random_list = [random.uniform(0, 1) for i in range(sum(sum_cln))]

        # enumerate column-sum and line-sum list
        enu_list_cln = list(enumerate(sum_cln))
        enu_list_ln = list(enumerate(sum_ln))

        # produce a list of lists containing the column position repeated as many times
        # as the corresponding column sum
        list_num_cln = [[pos for i in range(val)] for pos, val in enu_list_cln]
        # transform the list of list in one single list as long as the total sum
        one_list = [val for sublist in list_num_cln for val in sublist]

        # the list is zipped to the random number list (list with the same length)
        zipped_list = list(zip(random_list, one_list))

        # order the obtained list on the basis of the first element
        # of the list ie the random number
        zipped_list_ordered = sorted(zipped_list, key=lambda x: x[0])

        # create an empty matrix nl x nc
        mat_per = [[0 for i in range(len(sum_cln))] for k in range(len(sum_ln))]

        # for each line a line-sum interval is considered in the list created before :
        # inside each interval it check the column numbers found, the position obtained
        # [line-number][number found] is incremented by one
        s = 0
        for t in range(len(sum_ln)):
            rt = enu_list_ln[t][1]
            for u in range(rt):
                x = zipped_list_ordered[s + u][1]
                mat_per[t][x] += 1
            s += rt
        return mat_per
