# Student: [ID, name, sessions attended, sessions held, marks, events].
students = []
# Resource: [name, available quantity].
resources = [['Rooms', 5], ['Projectors', 3]]

def find_student(sid):
    for s in students:
        if s[0] == sid: return s
    return None

def summary():
    print('Students:', len(students))
    for sid, name, attended, held, marks, events in students:
        attendance = round(attended * 100 / held, 1) if held else 0
        average = round(sum(marks) / len(marks), 1) if marks else 0
        print(sid, name, 'attendance:', attendance, '%; average:', average, '; events:', events)
    print('Resources:', resources)

def menu():
    while True:
        print('\n1 Add student  2 Attendance  3 Marks  4 Event  5 Allocate resource  6 Summary  0 Exit')
        choice = input('Choice: ').strip()
        if choice == '0': break
        if choice == '1':
            sid = input('ID: ').strip()
            name = input('Name: ').strip()
            if not sid or not name or find_student(sid) is not None: print('Invalid or duplicate student')
            else:
                students.append([sid, name, 0, 0, [], []])
                print('Student added')
        elif choice in ('2', '3', '4'):
            s = find_student(input('Student ID: ').strip())
            if s is None:
                print('Student not found')
                continue
            if choice == '2':
                value = input('Present? (y/n): ').strip().lower()
                if value not in ('y', 'n'): print('Invalid attendance')
                else:
                    s[3] += 1
                    if value == 'y': s[2] += 1
                    print('Attendance recorded')
            elif choice == '3':
                raw = input('Mark (0-100): ').strip()
                if not raw.isdigit() or int(raw) > 100: print('Invalid mark')
                else:
                    s[4].append(int(raw))
                    print('Mark recorded')
            else:
                event = input('Event name: ').strip()
                if not event or event in s[5]: print('Invalid or duplicate event')
                else:
                    s[5].append(event)
                    print('Event registered')
        elif choice == '5':
            name = input('Resource name: ').strip()
            raw = input('Quantity: ').strip()
            found = False
            for item in resources:
                if item[0].lower() == name.lower():
                    found = True
                    if not raw.isdigit() or int(raw) <= 0 or int(raw) > item[1]: print('Invalid or unavailable quantity')
                    else:
                        item[1] -= int(raw)
                        print('Resource allocated')
            if not found: print('Resource not found')
        elif choice == '6': summary()
        else: print('Invalid menu choice')

menu()
