day = input()
 
daylist = ['SUN','MON','TUE','WED','THU','FRI','SAT']
 
for i, list in enumerate(daylist):
    if list == day and list == 'SUN':
        print(7)
    elif list == day:
        print(7-i)