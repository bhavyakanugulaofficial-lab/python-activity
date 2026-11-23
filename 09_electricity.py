# Units 1-100 at 2; next 100 at 3; remaining at 5; fixed charge 50.
def bill(units):
    if units < 0: return -1
    first = min(units, 100)
    second = min(max(units - 100, 0), 100)
    third = max(units - 200, 0)
    total = first * 2 + second * 3 + third * 5 + 50
    if units <= 100: total *= 0.9
    return round(total, 2)

# Apartment, consumption, previously recorded bill.
rows = [('A', 80, 189.0), ('B', 250, 800.0), ('C', 150, 400.0)]
ranking = []
for name, units, recorded in rows:
    calculated = bill(units)
    if calculated < 0:
        print(name, 'invalid consumption')
    else:
        print(name, 'bill:', calculated, 'discrepancy:', round(recorded - calculated, 2))
        ranking.append((units, name))
while ranking:
    best = 0
    for i in range(1, len(ranking)):
        if ranking[i][0] > ranking[best][0]: best = i
    units, name = ranking.pop(best)
    print('Rank:', name, units, 'units')
