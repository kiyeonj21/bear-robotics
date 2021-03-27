Implement a simple ATM controller
=================================
> code structure and usage

### A directory layout

    .
    ├── __init__.py
    ├── Pipfile        
    ├── main.py            # experiment and test file
    ├── bank.py            # bank class - createUser, addAccount, randomGenerator
    ├── transaction.py     # transaction class - insertCard, pinCheck, selectAccount, work, balance, deposit, withdraw
    └── README.md       
    
## File explanation
> main.py 
>
> This file is an experiment and test file. For convenient testing, I used a bank.db that was directly allocated in advance as follows: 
> ```{json}
> db = [
>        {
>            "name":'kiyeon Jeon',
>            "card_num":'1111-1111-1111-1111,
>            "password":'1234',
>            "accounts":[{'account_num': '111111111', 'balance': 1000},
>                        {'account_num': '111678000', 'balance': 100000}]
>        },
>        ...
> ]
> ```
> This test file (main.py) mainly consists of three parts: user creation, account addition, and transaction action.
> 1. create a user by appending a new user to the list of dictionaries (bank.db) with a randomly generated card number and account number.
> 2. add a randomly generated account number to the user's accounts.
> 3. test atm transaction task according to insertCard > pinCheck > selectAccount > task(balance, deposit, or withdraw) for the prepared target (name and card_num) and action (task, cash) jobs.  

> bank.py 
> 1. constructor - make user-defined db for convenient test. (It is also possible to test code with an empty bank.db, but the test instructions are more complicated.)
> 2. randomGenerator - generate a new card number or account number randomly excluding the number in bank.db
> 3. createUser - generate a random card number for new users
> 4. addAccount - add random account number to user account

> transaction.py 
> 1. constructor - get bank.db from bank instance
> 2. insertCard - given a name and card_num, return that dictionary 
> 3. pinCheck - check the password up to 5 times with the user dictionary obtained from insertCard function and return a boolean based on success or failure
> 4. selectAccount - select account number among user accounts
> 5. work (balance, deposit, withdraw) - calculate the account balance according to the operation (balance, deposit or withdrawal) and print the remaining balance

## Test example

```
==================================================
Test creating users...
==================================================
creating your account (Wanki Cho)
insert your password:
1212
Your account (name:Wanki Cho, card_num:7621-3045-7840-841, accounts_num:111191971) is created

creating your account (Minkyu Kim)
insert your password:
1313
Your account (name:Minkyu Kim, card_num:6071-8424-0076-523, accounts_num:111184736) is created

creating your account (Kiyeon Jeon)
You already have account. Do you create new user account?(Yes or No)
No
==================================================
Test adding accounts...
==================================================
adding new account on your card (Kiyeon Jeon,1234-1234-1234-1234)
[accounts_num:111619202] is added on your card [name:Kiyeon Jeon][card_num:1234-1234-1234-1234] 

adding new account on your card (Jeongyeol Kwon,1234-1234-1234-1289)
[accounts_num:111185599] is added on your card [name:Jeongyeol Kwon][card_num:1234-1234-1234-1289] 

adding new account on your card (Kiyeon Jeon,1234-1234-1234-1239)
There is no information on your name and card_num
==================================================
Test transaction actions...
==================================================
insert card (Kiyeon Jeon,1234-1234-1234-1234)
put your PIN number:
1234 << this password is decided by me in advance
PIN number is correct
Your accounts are ['111111111', '111678000', '111619202']
write account number that you want to work
111111111
Action 1: (balance,None)
111111111's balance is 1000

Action 2: (deposit,1000)
111111111's balance is 2000

Action 3: (withdraw,500)
111111111's balance is 1500

Action 4: (deposit,700)
111111111's balance is 2200

Action 5: (withdraw,3000)
Your account doesn't have enough cash!

==================================================
insert card (Jeongyeol Kwon,1234-1234-1234-1289)
put your PIN number:
1289 << this password is decided by me in advance
PIN number is correct
Your accounts are ['123111111', '111185599']
write account number that you want to work
123
You put wrong account number!!
123111111
Action 1: (balance,None)
123111111's balance is 2000

Action 2: (deposit,1000)
123111111's balance is 3000

Action 3: (withdraw,500)
123111111's balance is 2500

Action 4: (deposit,700)
123111111's balance is 3200

Action 5: (withdraw,3000)
123111111's balance is 200

==================================================
insert card (Kiyeon Jeon,1234-1234-1234-1230)
There is no information on your name and card_num
==================================================
```