from module import *


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
