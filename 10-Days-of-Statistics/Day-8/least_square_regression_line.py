import math
import statistics

X, Y = [], []
while True:
    try:
        x, y = input().split(" ")
        X.append(float(x))
        Y.append(float(y))
    except EOFError:
        break

def pearson_correlation_coefficient(X,Y):
    X_mean = statistics.mean(X)
    Y_mean = statistics.mean(Y)
    X_sd = statistics.pstdev(X)
    Y_sd = statistics.pstdev(Y)
    numerator = 0
    for i in range(len(X)):
        numerator += (X[i] - X_mean)*(Y[i] - Y_mean) 
    return numerator / (len(X) * X_sd * Y_sd)

b = pearson_correlation_coefficient(X,Y) * statistics.pstdev(Y) / statistics.pstdev(X)
a = statistics.mean(Y) - b * statistics.mean(X)

print(round(a + b * 80, 3))