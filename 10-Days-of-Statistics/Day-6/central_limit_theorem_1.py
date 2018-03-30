import math

def cdf(x, mean, sd):
    inner = 1 + math.erf((x - mean) / (sd * math.sqrt(2)))
    return 0.5 * inner

total_weight = float(input())
number_of_boxes = float(input())
mean_weight = float(input())
sd_weight = float(input()) 

sd_sample = sd_weight/math.sqrt(number_of_boxes) 

print (round(cdf(total_weight/number_of_boxes, mean_weight, sd_sample),4))