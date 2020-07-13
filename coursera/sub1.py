hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

gross = 0
if hours > 40 :
    gross = 40 * rate + (hours - 40) * 1.5*  rate
else :
    gross = hours * rate

print(gross)
