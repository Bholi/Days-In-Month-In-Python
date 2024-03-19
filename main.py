def is_leap_year(yea):
    if yea % 4 == 0:
        if yea % 100 == 0:
            if yea % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input('Enter the year : '))
month = int(input('Enter the month : '))


def day_in_month(y, m):
    if m > 12 or m < 1:
        return 'Invalid Month'
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(y) and m == 2:
        return 29
    return month_days[m - 1]


days = day_in_month(year, month)
print(days)
