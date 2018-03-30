import math

def cdf(x, mean, sd):
    inner = 1 + math.erf((x - mean) / (sd * math.sqrt(2)))
    return 0.5 * inner

no_sample = float(input())
mean = float(input())
sd = float(input())
percent = float(input())
z = float(input())

print (round(mean - z * (sd / math.sqrt(no_sample)),2))
print (round(mean + z * (sd / math.sqrt(no_sample)),2))