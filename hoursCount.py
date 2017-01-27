d = {}      # 'volunteer':[hours, 'fullname']
print('''first input:
a1 is alwaysOne, it will ensure each volunteer
gets or gets 1 hour added each time.
save will save the file.''')

while True:
    alwaysOne = 1
    n = input('Enter name of volunteer (firstname/nickname): ')
    if n == 'a1':
        alwaysOne = 0
    n = n.lower()
    if n == 'save':
        x = input(
            'Name of file to save (.txt is automatically added): '
            ) # Eg. Board meeting, x workshop
        x += '.txt'
        f = open(x, 'w')
        for v in d.values():
            fullName = v[0]
            tHours = str(v[1])
            eMail = v[2]
            f.write(fullName + ': ' + tHours + ' hour')
            if float(v[1]) > 1.0:
                f.write('s')
            f.write(', Email: ' + eMail)
            f.write('.\n')
        f.close()
        break
    if alwaysOne == 0:
        h = input('Enter number of hours: ')
    elif alwaysOne == 1:
        h = 1
    if n not in d.keys():
        fulln = ''
        fulln = input('full name of volunteer: ')
        fulln = fulln.title()
        email = input('Email? ')
        if email == 'n':
            email = 'none/not specified'
        d[n] = [fulln, float(h), email]
    else:
        oldh = float(d[n][0])
        d[n] = oldh + float(h)

'''
Things preferable to add:
- be able to undo
- re-prompt user input if user inputs something other than a simple string
'''