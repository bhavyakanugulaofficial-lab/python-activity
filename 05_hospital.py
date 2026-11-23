# Ward: name, occupied, capacity, staff, equipment, urgent waiting cases.
wards = [['A', 8, 10, 3, 1, 2], ['B', 10, 10, 6, 4, 3], ['C', 3, 8, 3, 2, 1]]
def audit(rows):
    priorities = []
    for row in rows:
        name, occupied, capacity, staff, equipment, urgent = row
        if occupied < 0 or capacity < 0 or occupied > capacity or staff < 0 or equipment < 0 or urgent < 0:
            print(name, ': invalid data')
            continue
        staff_need = (occupied + 3) // 4
        equipment_need = (occupied + 4) // 5
        bed_short = max(0, urgent - (capacity - occupied))
        staff_short = max(0, staff_need - staff)
        equip_short = max(0, equipment_need - equipment)
        print(name, 'shortages beds/staff/equipment:', bed_short, staff_short, equip_short)
        priorities.append((urgent, name))
    # Stable selection: largest urgency first; input order breaks ties.
    while len(priorities) > 0:
        best = 0
        for i in range(1, len(priorities)):
            if priorities[i][0] > priorities[best][0]: best = i
        urgent, name = priorities.pop(best)
        print('Priority:', name, 'urgent cases:', urgent)

audit(wards)
