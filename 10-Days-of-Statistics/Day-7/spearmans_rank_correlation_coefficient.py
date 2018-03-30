# Read Input
n = int(input())
X = [float(x) for x in input().split()]
Y = [float(x) for x in input().split()]

# Get the rank matrix
X_rank = [sorted(X).index(x) + 1 for x in X]
Y_rank = [sorted(Y).index(y) + 1 for y in Y]

d_sqr = [(x - y) ** 2 for (x, y) in zip(X_rank, Y_rank)]
spearmans_coeff = 1 - (6 * sum(d_sqr)) / (n**3 - n)

print(round(spearmans_coeff, 3))