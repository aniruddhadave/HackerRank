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
second_range = second.split(' ')


first_answer = cdf(float(first), mean, sd)
second_answer = cdf(float(second_range[1]), mean, sd) - cdf(float(second_range[0]), mean, sd)

print(first_answer)
print(second_answer)