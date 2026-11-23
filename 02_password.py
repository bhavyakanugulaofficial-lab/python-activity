def validate(password):
    failures = []
    upper = lower = digit = special = False
    for ch in password:
        if 'A' <= ch <= 'Z': upper = True
        elif 'a' <= ch <= 'z': lower = True
        elif '0' <= ch <= '9': digit = True
        elif ch in '!@#$%': special = True
    if len(password) < 8: failures.append('minimum length is 8')
    if not upper: failures.append('missing uppercase')
    if not lower: failures.append('missing lowercase')
    if not digit: failures.append('missing digit')
    if not special: failures.append('missing special character (!@#$%)')
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            failures.append('three consecutive identical characters')
            break
    for word in ('password', 'admin'):
        if word in password.lower(): failures.append('prohibited substring: ' + word)
    return failures

for sample in ('Abc123!x', 'aaaAdmin', 'Short1!'):
    errors = validate(sample)
    print(sample + ':', 'PASS' if len(errors) == 0 else '; '.join(errors))
