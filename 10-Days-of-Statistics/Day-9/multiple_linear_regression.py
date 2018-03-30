import numpy as np
m,n = [int(i) for i in input().strip().split(" ")]
X = []
Y = []
for i in range(n):
    data = input().strip().split(" ")
    X.append(data[:m])
    Y.append(data[m:])
q = int(input().strip())

X_test = []
for x in range(q):
    X_test.append(input().strip().split(" "))
X = np.array(X,float)
Y = np.array(Y,float)

# Normalize X, 
mean = np.mean(X, axis = 0)
sd = np.std(X, axis = 0)
X_normalized = (X - mean) 
X_test = np.array(X_test,float)
X_test_normalized = (X_test - mean) 

b = np.dot(np.linalg.inv(np.dot(X_normalized.transpose(),X_normalized)),np.dot(X_normalized.transpose(),Y - np.mean(Y)))

Y_test = np.dot(X_test_normalized , b) + np.mean(Y)

for i in Y_test:
    print(round(float(i),2))