import math
import statistics

size = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

def pearson_correlation_coefficient(X,Y):
    X_mean = statistics.mean(X)
    Y_mean = statistics.mean(Y)
    X_sd = statistics.pstdev(X)
    Y_sd = statistics.pstdev(Y)
    numerator = 0
    for i in range(0, size):
        numerator += (X[i] - X_mean)*(Y[i] - Y_mean) 
    return numerator / (size * X_sd * Y_sd)

print(round(pearson_correlation_coefficient(X,Y), 3))