class Transaction:
    def __init__(self, bank):
        self.db = bank.db

    def insertCard(self, name, card_num):
        print(f"insert card ({name},{card_num})")
        user = [each for each in self.db if each['card_num'] == card_num and each['name'] == name]
        if len(user)==0:
            print("There is no information on your name and card_num")
            return -1
        return user[0]
        # return (each for each in self.db if each['card_num'] == card_num and each['name'] == name).__next__()

    def pinCheck(self, user):
        print("put your PIN number:")
        cnt = 0
        while cnt < 5:
            password = input()
            if user['password'] == password:
                print("PIN number is correct")
                return True
            else:
                print("PIN number is wrong")
            cnt += 1
        print("You tried wrong PIN numbers five times!")
        return False

    def selectAccount(self, user):
        print("write account number that you want to work")
        while True:
            account_num=input()
            account = [each for each in user['accounts'] if each['account_num'] == account_num]
            if len(account)==0: print("You put wrong account number!!")
            else: break
        return account[0]
        # return (each for each in user['accounts'] if each['account_num'] == account_num).__next__()

    def work(self, account, task, cash=None):
        if task == 'balance':
            self.balance(account)
        elif task == 'deposit':
            self.deposit(account, cash)
        elif task == 'withdraw':
            self.withdraw(account, cash)

    def balance(self, account):
        print(f"{account['account_num']}'s balance is {account['balance']}\n")

    def deposit(self, account, cash):
        account['balance'] += cash
        print(f"{account['account_num']}'s balance is {account['balance']}\n")

    def withdraw(self, account, cash):
        if account['balance']-cash<0:
            print("Your account doesn't have enough cash!\n")
            return
        account['balance'] -= cash
        print(f"{account['account_num']}'s balance is {account['balance']}\n")