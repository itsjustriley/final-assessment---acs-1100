# NOTES
# Hi Mitchell! Just wanted to leave a few notes
# Super swamped with school + dev degree, so I didn't have time to polish this the way I'd like to BUT
# thought i'd list out some potential improvements I'm aware could be made and don't have time for:
#   - validate that the input for amounts is a number - it breaks right now if it's not
#   - round to two decimals
#   - change the displayed  message when the main while loop restarts so it doesn't say welcome every time
#   - write to the .txt file so the data is preserved when the app is exited
#   - some formatting inconsistencies 
#   - could probably write a mini function to ask for an amount and validate that since I do that often
#   - could have made better use of objects vs lists
#   - hide password input
#   - for security reasons I should probably wait until I have the password/username combo to validate
#
#   as of right now if you run this it'll show you the list of users and their details (formatted)
#   then run accrue_interest() and display the list again to show it works
#   then I popped the rest of the functions into a banking app function. 
#   looking forward to your feedback, and thanks for a great term!

# CORE ASSESSMENT
# get users (read data, return an array of user arrays based on lines in txt file)
def get_users(filename):
    user_data = [] 
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            user_data.append(line)

    return user_data

user_list = get_users('data.txt')

# prompting for username, validating
def enterUsername():
    user_username = ''
    while user_username == '':
        user_username = input('Enter your username: ')
        if any(user_username == user[0] for user in user_list):
            return user_username
        else:
            user_username = ''
            print('invalid username')

# prompting for password, validating based on username
def enterPassword(user_username):
    valid_password = False
    while valid_password == False:
        user_password = input('Enter your password: ')
        for user in user_list:
            if user_username in user[0] and user_password in user[1]:
                valid_password = True
        if valid_password == False:
            print('Invalid password.')
    return valid_password

# login function that calls the username and password functions, returns a user info dictionary
def login():
    user_dictionary = {
        'username': '',
        'name': '',
        'balance': ''
    }
    username = enterUsername()
    if enterPassword(username) == True: 
            for user in user_list:
                if username in user[0]:
                    user_dictionary['username'] = user [0]
                    user_dictionary['name'] = user[2]
                    user_dictionary['balance'] = user[3]
                    
    return user_dictionary

# function to put it all together and display the information
def display_info():
    user_info = login()
    name = user_info['name']
    balance = user_info['balance']
    print(f'Name: {name}')
    print(f'Balance: {balance}')


# function to display user info that takes an array and returns a formatted string
def show_users(user_list):
    user_string = []
    for user in user_list:
        username = user[0]
        password = user[1]
        name = user[2]
        balance = user[3]
        user_string.append(f'Username: {username}, Password: {password}, Name: {name}, Balance: {balance}')
    user_string = '\n'.join(user_string)
    return user_string


# STRETCH GOALS
# accrue interest
def accrue_interest(interest_rate):
    for user in user_list: 
        balance = float(user[3])
        balance += balance * interest_rate
        user[3] = str(balance)  


def deposit(old_balance):
    amount = float(input('Enter an amount to deposit: '))
    balance = old_balance + amount
    return balance

def withdraw(old_balance):
    valid_amount = False
    while valid_amount == False:
        amount = float(input('Enter an amount to withdraw: '))
        if amount > old_balance:
            print('Your balance is too low.')
        else:
            valid_amount = True
    balance = old_balance - amount
    return balance

def transfer(username, old_balance):
    valid_amount = False
    while valid_amount == False:
        amount = float(input('Enter an amount to transfer: '))
        if amount > old_balance:
            print('Your balance is too low.')
        else:
            valid_amount = True
    valid_recipient = False
    while valid_recipient == False:
        recipient = input('Please enter the username of the person you wish to transfer the funds to: ')
        if (any(user[0] == recipient for user in user_list)):
            if username != recipient:
                valid_recipient = True
        else:
            print('Invalid recipient')

    for user in user_list:
        if user[0] == recipient:
            user[3] = float(user[3]) + amount
    balance = old_balance - amount
    print(f'You have transfered ${amount} to {recipient}')
    return balance


def bank_app():
    user_info = login()
    name = user_info['name']
    balance = float(user_info['balance'])
    banking = True
    while banking == True:     
        print(f'Welcome, {name}.')
        print(f'Balance: {balance}')
        print('Choose an option:')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Transfer')
        print('4. Exit')
        choice = input('> ')
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance = withdraw(balance)
        elif choice == '3':
            balance= transfer(name, balance)
        elif choice == '4':
            print('Thank you! Have a great day!')
            return 
        else:
            print('invalid choice')
        print('Your balance has been updated.')

print(show_users(user_list))
accrue_interest(.10)
print(show_users(user_list))
bank_app()