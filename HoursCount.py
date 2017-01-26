'''
Structure:
- while True loop.
- asks for nickname or name you do not mind typing repeatedly
- asks for amount of volunteering hours.
- if name is not in the dict, prompts full name of volunteer.
    - makes the nickname the key, [number of hours, full name] as list
- if it is in the dict, just adds the amount of hours.
- when prompted nickname of volunteer, typing in "save" allows you to save
    the recorded names and hours like this:
        Full Name: x hour(s)
    - lets be honest if you nicknamed a friend "save" then you should probably
        know better
- name the save file.
- breaks the while true loop.
'''
d = {}      # 'volunteer':[hours, 'fullname']
print('''This program allows the user to input the name
of a volunteer and the amount of hours they put
in for a certain recurring event (which will be
saved as a file in the place where this file is.)''')
while True:
    n = input('Enter name of volunteer (firstname/nickname): ')
    n = n.lower()
    if n == 'save':
        x = input(
            'Name of file to save (.txt is automatically added): ') # Eg. Board meeting, x workshop
        x += '.txt'
        f = open(x, 'w')
        for k in d:
            s = str(d[k][0])
            f.write(d[k][1] + ': ' + s + ' hour')
            if int(d[k][0]) > 1:
                f.write('s')
            f.write('\n')
        f.close()
        print(d)
        break
    h = input('Enter number of hours: ')
    if n not in d.keys():
        fulln = ''
        fulln = input('full name of volunteer: ')
        d[n] = [int(h), fulln]
    else:
        d[n] = d[n][0] + int(h)

'''
Things preferable to add:
- be able to undo
- re-prompt user input if user inputs something other than a simple string
'''
