import math

def cdf(x, mean, sd):
    inner = 1 + math.erf((x - mean) / (sd * math.sqrt(2)))
    return 0.5 * inner

total_tickets = float(input())
number_of_students = float(input())
mean_tickets = float(input())
sd_tickets = float(input()) 

sd_sample = sd_tickets/math.sqrt(number_of_students) 

print (round(cdf(total_tickets/number_of_students, mean_tickets, sd_sample),4))