import random
from textwrap import wrap

class Bank:
    def __init__(self):
        self.db = [
            {
                'name': 'Kiyeon Jeon',
                'card_num': '1234-1234-1234-1234',
                'password': '1234',
                'accounts': [{'account_num': '111111111', 'balance': 1000},
                             {'account_num': '111678000', 'balance': 100000}]
            },
            {
                'name': 'Jeongyeol Kwon',
                'card_num': '1234-1234-1234-1289',
                'password': '1289',
                'accounts': [{'account_num': '123111111', 'balance': 2000}]
            },
            {
                'name': 'Kiyeon Jeon',
                'card_num': '1278-1234-1234-1200',
                'password': '5634',
                'accounts': [{'account_num': '111231111', 'balance': 5000}]
            }
        ]

    def randomGenerator(self, type):
        if type == 'card':
            max_num = 10 ** 16
            card_nums = list((each['card_num'] for each in self.db))
            nums = [each.replace('-', '') for each in card_nums]
        else:
            max_num = 10 ** 9
            nums = [account['account_num'] for each in self.db for account in each['accounts']]
        nums = list(map(int, nums))
        nums.sort()
        interval = []
        for idx, each in enumerate(nums):
            if idx == 0:
                interval.append((0, each))
            elif idx == len(nums) - 1:
                interval.append((each, max_num))
            else:
                interval.append((nums[idx - 1] + 1, each))
        num = random.choice(range(*random.choice(interval)))
        if type == 'card':
            num = '-'.join(wrap(str(num), 4))
        else:
            num = str(num)
        return num

    def createUser(self, name):
        print(f"creating your account ({name})")
        # check if user already has account
        if name in set([each['name'] for each in self.db]):
            print("You already have account. Do you create new user account?(Yes or No)")
            op = input().capitalize()
            if op !="Yes":
                return
        # card_num and account_num generator
        card_num = self.randomGenerator('card')
        account_num = self.randomGenerator('account')

        # create password

        print("insert your password:")
        password = input()
        print(f'Your account (name:{name}, card_num:{card_num}, accounts_num:{account_num}) is created\n')
        self.db.append({'name': name,
                        'card_num': card_num,
                        'password': password,
                        'accounts': [{'account_num': account_num, 'balance': 0}]
                        })

    def addAccount(self, name, card_num):
        print(f"adding new account on your card ({name},{card_num})")
        # user = (each for each in self.db if each['card_num'] == card_num and each['name'] == name).__next__()
        user = [each for each in self.db if each['card_num'] == card_num and each['name'] == name]
        if len(user)==0:
            print(f"There is no information on your name and card_num")
            return
        # user = [each for each in self.db if each['card_num'] == card_num and each['name'] == name][0]
        # account_num generator
        account_num = self.randomGenerator('account')
        user[0]['accounts'].append({'account_num': account_num, 'balance': 0})
        print(f'[accounts_num:{account_num}] is added on your card [name:{name}][card_num:{card_num}] \n')