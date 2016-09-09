daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    if year %4 == 0:
        if year %100 == 0 and year %400 != 0:
            return False
        return True
    return False

def is_date1_first(year1, month1, day1, year2, month2, day2):
    if year2 >= year1:
        if month2 >= month1:
            if day2 >= day1:
                return True
            return False
        return False
    return False

#(year1, month1, day1, year2, month2, day2) = (2011,6,30,2012,6,30)
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = daysOfMonths[month1 - 1] - day1
    month1 += 1
    while month1 < month2:
        days += daysOfMonths[month1]
        month1 += 1
    while year1 < year2:
        if is_leap_year(year1):
            days += 366
        else:
            days += 365
        year1 += 1
    days += day2
    return days





print daysBetweenDates(2012,1,1,2012,2,28)
print daysBetweenDates(2012,1,1,2012,3,1)
print daysBetweenDates(2011,6,30,2012,6,30)
print daysBetweenDates(2011,1,1,2012,8,8)
print daysBetweenDates(1900,1,1,1999,12,31)

# (2012,1,1,2012,2,28)  58
# (2012,1,1,2012,3,1)  60
# (2011,6,30,2012,6,30)  366
# (2011,1,1,2012,8,8)  585
# (1900,1,1,1999,12,31)  36523
