import math

def cdf(x, mean, sd):
    inner = 1 + math.erf((x - mean) / (sd * math.sqrt(2)))
    return 0.5 * inner

inputs = input()
first = input()
second = input()

inputs = inputs.split(' ')
mean = float(inputs[0])
sd = float(inputs[1])



first_answer = (1 - cdf(float(first), mean, sd)) * 100
second_answer = (1 - cdf(float(second), mean, sd)) * 100
third_answer = cdf(float(second), mean, sd) * 100

print("%.2f" %first_answer)
print("%.2f" %second_answer)
print("%.2f" %third_answer)