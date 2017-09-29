current_users = ['Mina', 'Tina', 'Rina', 'Lina', 'Admin']
new_users = ['Mihir', 'Amit', 'Mina', 'Tina']

for user in new_users:
    if user in current_users:
        print('\n' + str(user) + ' has to provide different name.')
    else:
        print('\n' + str(user) + ' is an available name.')
