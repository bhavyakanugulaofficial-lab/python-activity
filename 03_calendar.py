def calendar(start, days):
    # Monday = 0, Sunday = 6. February/leap-year validity is caller's responsibility.
    if start < 0 or start > 6 or days not in (28, 29, 30, 31):
        print('Invalid weekday or month length')
        return
    print('Mo Tu We Th Fr Sa Su')
    day = 1
    first_week = True
    while day <= days:
        week = ''
        for weekday in range(7):
            if first_week and weekday < start:
                week += '   '
            elif day <= days:
                week += str(day).rjust(2) + ' '
                day += 1
        print(week.rstrip())
        first_week = False


calendar(3, 30)
print('Invalid test:')
calendar(7, 30)
