def audit(opening, transactions):
    if opening < 0:
        print('Invalid opening balance')
        return
    balance = opening
    last_kind = ''
    last_amount = 0
    streak = 0
    for kind, amount in transactions:
        if kind == last_kind and amount == last_amount:
            streak += 1
        else:
            streak = 1
        last_kind, last_amount = kind, amount
        if kind not in ('deposit', 'withdrawal', 'transfer') or amount <= 0:
            print(kind, amount, 'REJECTED: invalid operation or amount')
        elif kind != 'deposit' and amount > balance:
            print(kind, amount, 'REJECTED: insufficient funds')
        else:
            if kind == 'deposit': balance += amount
            else: balance -= amount
            print(kind, amount, 'ACCEPTED; balance:', balance)
        if streak == 3 and kind in ('withdrawal', 'transfer') and amount > 0:
            print('ALERT: three identical consecutive outgoing attempts')
    print('Final balance:', balance)

audit(1000, [('deposit', 500), ('withdrawal', 200), ('withdrawal', 200), ('withdrawal', 200), ('transfer', 2000), ('deposit', -1)])
