def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
start,end=map(int, input().split())
for year in range(start,end+1):
    if is_leap_year(year):
        print(year,end=' ')