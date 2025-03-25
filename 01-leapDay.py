def is_leap(year):
    leap = False
    if(year%400==0):
        leap=True
    elif(year%4==0 and not(year%100==0)):
        leap=True
    return leap

year = 2028
print(is_leap(year))