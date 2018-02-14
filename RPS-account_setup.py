print('RPS Account Setup')
while True:
    username = input('Pick a Username: ')
    password = input('Pick a Password: ')
    password_confirm = input('Re-enter password to confirm: ')
    if password == password_confirm:
        print('Your account has been setup')
        text_file = open('accounts.txt','a')
        text_file.write("\n")
        text_file.write(username)
        text_file.write('\n')
        text_file.write(password)
        text_file.close()
        break
    if password != password_confirm:
        print('Your passwords mismatch. Please try again')

