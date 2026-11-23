# All times are (day number, hour, minute); one day is 24 hours.
entry = (1, 22, 0)
exit_time = (2, 2, 30)
vehicle = 'car'
lost_ticket = False
rates = [('bike', 10), ('car', 20), ('truck', 40)]

def minutes(t):
    day, hour, minute = t
    if day < 1 or hour < 0 or hour > 23 or minute < 0 or minute > 59:
        return -1
    return (day - 1) * 1440 + hour * 60 + minute

def parking_fee(start, end, category, penalty):
    a, b = minutes(start), minutes(end)
    rate = 0
    for name, value in rates:
        if name == category:
            rate = value
    if a < 0 or b < 0 or b <= a or rate == 0:
        return 'Invalid time, interval, or category'
    duration = b - a
    full_days = duration // 1440
    remainder = duration % 1440
    # Each started hour costs rate; each 24-hour block is capped at 10 hours.
    hours = (remainder + 59) // 60
    if hours > 10:
        hours = 10
    fee = (full_days * 10 + hours) * rate
    if penalty:
        fee += 100
    return fee

print('Parking fee:', parking_fee(entry, exit_time, vehicle, lost_ticket))
print('Invalid interval:', parking_fee((1, 12, 0), (1, 11, 0), 'car', False))
print('Daily cap and penalty:', parking_fee((1, 0, 0), (2, 0, 0), 'car', True))
