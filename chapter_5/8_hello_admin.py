user_names = ['Mina', 'Tina', 'Rina', 'Lina', 'Admin']
for name in user_names:
    if name == 'Admin':
        print('Hello ' + str(name) + ', ' + 'would you like to see a status report?')
    else:
        print('Hello ' + str(name) + ', ' + 'thank you for logging in again.')