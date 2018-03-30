from sklearn import linear_model

m,n = input().split(" ")
inputs = []
for i in range(int(n)):
    inputs.append([float(j) for j in input().split(" ")])

y = [x.pop() for x in inputs]
q = int(input())
x_test = []

for i in range(q): 
    x_test.append([float(j) for j in input().split(" ")])

model = linear_model.LinearRegression()
model.fit(inputs, y)
a = model.intercept_
b = model.coef_

for m in range(0, len(x_test)):
    y_pred = a + x_test[m][0] * b[0] + x_test[m][1] * b[1]
    print (y_pred)
