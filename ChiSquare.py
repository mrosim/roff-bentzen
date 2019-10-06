import utils as u


class ChiSquare:

    def __init__(self, input_matrix):
        self.input_matrix = input_matrix

    def sum_line(self):
        sum_lines = u.sub_matrix_sumi(self.input_matrix)
        return sum_lines

    def sum_column(self):
        inner = u.transpose(self.input_matrix)
        sum_column = u.sub_matrix_sumi(inner)
        return sum_column

    def expected_matrix(self):
        tot = sum(self.sum_line())
        mat_exp = [[x * y / tot for y in self.sum_column()] for x in self.sum_line()]
        return mat_exp

    def chi_square_bycell(self):
        chi_matrix = [
            [((float(o) - float(e)) ** 2) / float(e) for (o, e) in zip(self.input_matrix[i], self.expected_matrix()[i])]
            for i, v in enumerate(self.input_matrix)]
        return chi_matrix

    def chi_square_tot(self):
        matrice_attesa = self.expected_matrix()
        chi_matrice = self.chi_square_bycell()
        chi_square_par = u.sub_matrix_sumf(chi_matrice)
        return sum(chi_square_par)
