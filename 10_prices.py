def analyse(products, threshold):
    if threshold < 0:
        print('Invalid threshold')
        return
    for name, prices in products:
        valid = len(prices) >= 2
        for price in prices:
            if price <= 0: valid = False
        if not valid:
            print(name, 'invalid price history')
            continue
        maximum = -1
        period = 0
        for i in range(1, len(prices)):
            change = (prices[i] - prices[i - 1]) * 100 / prices[i - 1]
            print(name, 'period', i, 'change:', round(change, 2), '%')
            if abs(change) > maximum:
                maximum = abs(change)
                period = i
        print(name, 'max absolute change:', round(maximum, 2), '% at period', period, '; flagged:', maximum > threshold)

analyse([('Rice', [100, 120, 90]), ('Milk', [50, 55, 60]), ('Oil', [0, 5])], 20)
