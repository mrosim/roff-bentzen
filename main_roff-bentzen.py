from chi_square import ChiSquare
from matrix_perm import Permutation
import random
import math
# number of permutations
nperm = 1000
# open the input file  
with open('example.txt', 'r') as matrice:
    mat_oss = [i.split() for i in matrice]
# call the class chi-square for the observed matrix
tc = ChiSquare(mat_oss)
print(mat_oss)
# calculate the chi-square for the observed matrix
x = tc.chi_square_tot()
print('X2-observed =',x)
# iterate N times a permutation, calculating the chi-square for each,
# and comparing to the true one
xvalues=[]
for t in range(nperm):
    pr = Permutation(mat_oss)
    perm_matrix = pr.perm()
    pmc = ChiSquare(perm_matrix)
    xper = pmc.chi_square_tot()
    if xper > x:
        xvalues.append(xper)
print(xvalues)
n_rand_hchi = len(xvalues)
pval = n_rand_hchi/nperm
serr = math.sqrt(pval*(1-pval)/nperm)
print('X2 p-value =',pval,'SE:',serr)





