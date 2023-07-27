import pandas as pd

class Bank:
    def __init__(self):
        #card/pin/account/balance data in dataframe
        data = {
            'card' : ['0000 0000 0000 0000', '1111 1111 1111 1111', '1111 1111 1111 1111', '2222 2222 2222 2222', '3333 3333 3333 3333', '3333 3333 3333 3333', '3333 3333 3333 3333'],
            'pin' : ['1234', '3945', '3945', '1254', '8989', '8989', '8989'],
            'account' : ['110-110-111111', '110-112-333333', '110-283-282839', '110-333-444444', '110-283-283826', '210-382-383619', '220-333-222222'],
            'balance' : [35, 745, 122, 923, 1283, 19, 363]
        }
        
        self.data = pd.DataFrame(data)

    def check_card(self, card_num):
        # check if card is valid
        if (self.data['card'] == card_num).any():
            return True
        else:
            return False
    
    def check_pin(self, card_num, pin):
        # check if the pin number is correct
        if (self.data[self.data['card'] == card_num]['pin'] == pin).any():
            return True
        else:
            return False
    
    def show_accounts(self, card_num):
        # show accounts connected to the card
        return self.data[self.data['card'] == card_num]['account'].tolist()
    
    def check_balance(self, card_num, account):
        # check the balance
        matching_row = self.data[(self.data['card'] == card_num) & (self.data['account'] == account)]
        return matching_row['balance'].values[0]
    
    def deposit(self, card_num, account, money):
        # deposit
        mask = (self.data['card'] == card_num) & (self.data['account'] == account)
        self.data.loc[mask, 'balance'] += money
        return True

    def withdraw(self, card_num, account, money):
        # withdraw
        mask = (self.data['card'] == card_num) & (self.data['account'] == account)
        self.data.loc[mask, 'balance'] -= money
        return True

class AutoInput:
    """
    just to test
    """
    def __init__(self, inputs):
        self.inputs = inputs

    def __call__(self, *args, **kwargs):
        return self.inputs.pop(0)

class ATM:
    def __init__(self, auto = False, input_values = None):
        self.account = None
        self.cardnumber = None
        self.pin = None
        self.bank = Bank()

        if auto:
            input_func = AutoInput(input_values)
            # Python 3.x
            import builtins
            builtins.input = input_func

        # initiate from card insertion
        self.insert_card()

    def insert_card(self):
        # get card info from user
        print("\nInsert the card (card number)")
        card_num = input()
        # check if the card is valid
        if self.bank.check_card(card_num):
            self.cardnumber = card_num
            # if valid request pin
            return self.insert_pin()
        else:
            # if not re-ask for the card info
            print("\nInvalid card.\n")
            return self.insert_card()
    
    def insert_pin(self):
        # request pin number
        print("\nEnter PIN number.")
        pin = input()
        # check if pin is correct
        if self.bank.check_pin(self.cardnumber, pin):
            self.pin = pin
            # if correct
            return self.choose_account()
        else:
            # if not re-ask for the pin number
            print("\nWrong PIN.\n")
            return self.insert_pin()

    def choose_account(self):
        # request to choose account
        print("\nChoose account to progress (enter number)")
        # print out all accounts connected to the card
        accounts = self.bank.show_accounts(self.cardnumber)
        for i in range(len(accounts)):
            print(i,':', accounts[i])
        try:
            account_num = int(input())
            if account_num < len(accounts):
                # if account is selected, go to transaction
                self.account = accounts[account_num]
                return self.choose_action()
            else:
                # if account selection is wrong, re-ask to select
                print("\nWrong account selection.\n")
                return self.choose_account()
        except:
            # if account selection is wrong, re-ask to select
            print('\nInvalid input\n')
            return self.choose_account()

    def choose_action(self):
        # request to choose transaction
        print("\nSelect transaction (1. See Balance  2. Deposit  3. Withdraw  0. Exit)")
        action = input()
        if action == '1':
            # see balance
            return self.see_balance()
        elif action == '2':
            # deposit
            return self.deposit()
        elif action == '3':
            # withdraw
            return self.withdraw()
        elif action == '0':
            # end
            print("\nThanks for your use.")
            return True
        else:
            # wrong selection, re-ask to select
            print("\nPlease select from the transaction.\n")
            return self.choose_action()
        
    def see_balance(self):
        # show balance
        balance = self.bank.check_balance(self.cardnumber, self.account)
        print("\nCurrent balance of {} is ${}\n".format(self.account, balance))
        # go back to select transaction
        return self.choose_action()
    
    def deposit(self):
        # request to enter the amount of money to deposit
        print("\nInsert money to deposit (in form of integer)")

        # get input(amount of money to deposit) from user
        try:
            money = int(input())
            # deposit and see balance after the deposit
            self.bank.deposit(self.cardnumber, self.account, money)
            print("\nDeposit Completed\n")
            self.see_balance()
        except:
            # wrong input
            print("\nWrong amount of money!\n")
            return self.deposit()
    
    def withdraw(self):
        # request to enter the amount of money to withdraw
        print("\nEnter amount of money to withdraw (in form of integer)")
        try:
            # get input(amount of money to withdraw) from user
            money = int(input())
            # case of enough balance
            if self.bank.check_balance(self.cardnumber, self.account) < money:
                print("\nNot enough balance to withdraw\n")
            # case of not enough balance
            else:
                self.bank.withdraw(self.cardnumber, self.account, money)
                print("\nWithdrawal Completed\n")
            # for both case, show balance
            self.see_balance()
        except:
            # wrong input
            print("\nWrong amount of money!\n")
            return self.withdraw()
        


if __name__ == "__main__":
    """
    for the test


    data of card-pin-account-balance
                      card   pin         account  balance
    0  0000 0000 0000 0000  1234  110-110-111111       35
    1  1111 1111 1111 1111  3945  110-112-333333      745
    2  1111 1111 1111 1111  3945  110-283-282839      122
    3  2222 2222 2222 2222  1254  110-333-444444      923
    4  3333 3333 3333 3333  8989  110-283-283826     1283
    5  3333 3333 3333 3333  8989  210-382-383619       19
    6  3333 3333 3333 3333  8989  220-333-222222      363
    """
    
    # Define the input values for testing
    print("Testing work flow, card-pin-account-balance")
    input_values = [
        "1111 1111 1111 1111",  # Card number
        "3945",                 # PIN
        "0",                    # Account
        "1",                    # Transaction 1-balance
        "0",                    # 0-Exit
    ]
    ATM(True, input_values)
    print("********************\n\n")


    print("Testing work flow wrong card-card-pin-account-deposit")
    input_values = [
        "4928 9392 4040 1923",  # Wrong card number
        "3333 3333 3333 3333",  # Card number
        "8989",                 # pin
        "1",                    # account
        "2",                    # 2-deposit
        "100",                  # amount of deposit
        "0"                     # 0-exit
    ]
    ATM(True, input_values)
    print("********************\n\n")

    print("Testing work flow card-wrong pin-pin-account-withdraw")
    input_values = [
        "2222 2222 2222 2222",  # card number
        "1234",                 # wrong pin
        "1254",                 # pin
        "0",                    # account
        "3",                    # 3-withdraw
        "20",                   # amount of withdraw
        "0"                     # 0-exit
    ]
    ATM(True, input_values)
    print("********************\n\n")


    # If you want to test manually, uncomment the code below
    # ATM()
