print('\nSorry to announce that we can only invite two people as our bigger table has not arrived.')
guest_list = ['Amit Pandey', 'Vijayan', 'Ekta Jee']
message = ', we are excited to inform you that you would be meeting more people at dinner as we have got a bigger table'

guest_list.append('Sumit Jee')
guest_list.insert(1, 'Biltu')
print('\nHi ' + guest_list[0] + message)
print('\nHi ' + guest_list[1] + message)
print('\nHi ' + guest_list[2] + message)
print('\nHi ' + guest_list[3] + message)

first_guest = guest_list.pop(0)
print('first guest: ' + first_guest)
second_guest = guest_list.pop(1)
print('second guest: ' + second_guest)

print('\nHi ' + guest_list[0] + message)
print('\nHi ' + guest_list[1] + message)

del guest_list[0]
del guest_list[1]

print('length of guest list: ' + str(len(guest_list)))