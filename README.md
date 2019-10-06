# roff-bentzen
The chi-square value of a matrix m x n (observed values) is compared with the chi-square values of N permutations of the same matrix (raw and column sums kept constant). p-value is obtained by the rate between the number of times in which the permuted matrices have higher chi-square values and the total number of permutations. Standard error of p-value is calculated as well.

In the main.py file  you have to set the numebr of permutations and the input file matrix.
The input file matrix is a .txt file with numbers separated by spaces.

Roff and Bentzen, Molecular Biology and Evolution 6(5):539-45 · October 1989
Significance levels obtained from a chi 2 contingency test are suspect when sample sizes are small. Traditionally this has meant that data must be combined. However, such an approach may obscure heterogeneity and hence potentially reduce the power of the statistical test. In this paper, we present a Monte Carlo solution to this problem: by this method, no lumping of data is required, and the accuracy of the estimate of alpha (i.e., a type 1 error) depends only on the number of randomizations of the original data set. We illustrate this technique with data from mtDNA studies, where numerous genotypes are often observed and sample sizes are relatively small.
