

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return  f'Mr {self.name} your balance {self.balance}'
    
    def deposite(self, amount):
        # if amount <= 0:
        #     return f' Mr/Mrs/Miss {self.name} this transaction is an invalid transaction'
        # elif amount > 0:
        self.balance += amount
        return f'Mr {self.name} your balance {self.balance}'
    
    def withdraw(self, amount):
        self.balance -= amount
        # if amount < self.balance:
        #     return f'Mr/Mrs/Miss {self.name} you have an insufficient amount to withdraw'
        # else:
        return f' Mr/Mrs/Miss {self.name} you transaction was successful and your balance is {self.balance}'
print('Welcome to Zenith Bank')    
info=input('Enter you name     \n')
user1=Account(info)
print(user1)

while True:
    choice=input('''
            What do you want to?
            D for deposite:
            W for withdraw
            B for balance     
    ''')
    if choice == 'B'.lower():
        print(user1)
    elif choice == 'D'.lower():
        amount=int(input('Enter the amount to deposite'))
        if amount <= 0:
            print('Invalid amount entered')
        else:
            print(user1.deposite(amount))
    elif choice == 'W'.lower():
        amount = int(input('Enter the amount to'))
        if amount <= 0:
            print('Invalid amount entered')
        else:
            print(user1.withdraw(amount))
    question=input('Do you want to continue? y/n ')
    if question == 'y':
        continue
    else:
        print('Thanks for banking with us. Have a nice day')
        break
            
        

