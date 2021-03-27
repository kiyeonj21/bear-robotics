import sys
from bank import Bank
from transaction import Transaction


if __name__ == '__main__':
    bank = Bank()
    trans = Transaction(bank)
    print("=" * 50)

    # create users
    print("Test creating users...")
    print("=" * 50)
    bank.createUser(name="Wanki Cho")
    bank.createUser(name="Minkyu Kim")
    bank.createUser(name="Kiyeon Jeon")  # already exisiting name
    print("="*50)

    # add accounts
    print("Test adding accounts...")
    print("=" * 50)
    bank.addAccount(name="Kiyeon Jeon", card_num='1234-1234-1234-1234')
    bank.addAccount(name="Jeongyeol Kwon", card_num='1234-1234-1234-1289')
    bank.addAccount(name="Kiyeon Jeon", card_num='1234-1234-1234-1239')  # wrong card_num
    print("=" * 50)

    # transaction actions
    print("Test transaction actions...")
    print("=" * 50)
    targets = [('Kiyeon Jeon', '1234-1234-1234-1234'),
               ('Jeongyeol Kwon', '1234-1234-1234-1289'),
               ('Kiyeon Jeon', '1234-1234-1234-1230')   # wrong card_num
               ]
    actions = [('balance', None),
               ('deposit', 1000),
               ('withdraw', 500),
               ('deposit', 700),
               ('withdraw', 3000)   # not enough money in some cases
               ]

    for name, card_num in targets:
        # insert card
        user = trans.insertCard(name=name, card_num=card_num)
        if user==-1: continue

        # pin check
        if not trans.pinCheck(user=user):
            sys.exit(0)

        # select account
        account_nums = [each['account_num'] for each in user['accounts']]
        print(f"Your accounts are {account_nums}")
        account = trans.selectAccount(user=user)
        for idx, (task, cash) in enumerate(actions):
            print(f"Action {idx+1}: ({task},{cash})")
            trans.work(account=account, task=task, cash=cash)
        print("=" * 50)
    print("=" * 50)
