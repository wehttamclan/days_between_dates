daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    if year %4 == 0:
        if year %100 == 0 and year %400 != 0:
            return False
        return True
    return False

def is_date1_first(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    if year2 == year1:
        if month2 > month1:
            return True
        if month2 == month1:
            return day2 > day1
    return False


def nextDay(year, month, day):
    year, month, day = year, month, day + 1
    if is_leap_year(year):
        daysOfMonths[1] = 29
    if day > daysOfMonths[month - 1]:
        year, month, day = year, month + 1, 1
    if month > 12:
        year, month, day = year + 1, 1, 1
    return year, month, day



def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while is_date1_first(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
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


#the following procedures are for a method that counts everyday from date1 to date2.
#def nextDay(year, month, day)   #perhaps act on and return a tuple.

#try to update the while loops with a procedure that determines stopping conditions.
