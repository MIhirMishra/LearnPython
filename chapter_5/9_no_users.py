user_names = []
if user_names.__len__() > 0:
    for name in user_names:
        if name == 'Admin':
            print('Hello ' + str(name) + ', ' + 'would you like to see a status report?')
        else:
            print('Hello ' + str(name) + ', ' + 'thank you for logging in again.')
else:
    print('\nWe need to find some users')
