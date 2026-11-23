# Product order: water, food. Area: name, urgency (larger first), requirements.
def allocate(stock, areas):
    for amount in stock:
        if amount < 0:
            print('Invalid stock')
            return
    for name, urgency, needs in areas:
        if urgency < 0 or len(needs) != len(stock):
            print('Invalid area:', name)
            return
        for n in needs:
            if n < 0:
                print('Invalid demand:', name)
                return
    remaining = stock[:]
    queue = areas[:]
    while len(queue) > 0:
        best = 0
        for i in range(1, len(queue)):
            if queue[i][1] > queue[best][1]: best = i
        name, urgency, needs = queue.pop(best)
        given = []
        unmet = []
        for i in range(len(stock)):
            amount = min(remaining[i], needs[i])
            remaining[i] -= amount
            given.append(amount)
            unmet.append(needs[i] - amount)
        print(name, 'allocated:', given, 'unmet:', unmet)
    print('Stock remaining:', remaining)

allocate([10, 8], [('North', 2, [6, 5]), ('South', 5, [7, 6]), ('East', 1, [2, 3])])
