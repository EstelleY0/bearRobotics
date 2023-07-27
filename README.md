# bearRobotics
bear robotics coding test project

A simple ATM program,
written in python 3.10.11.
Python 3 is required, may not work properly in previous versions.

------

## Code detail


#### module


1. Bank


    check_card : check if card is valid or not
  

    check_pin : check if pin number is correct or not
  

    show_accounts : show all accounts connected to the card
  

    check_balance : check the balance of the account
  

    deposit : modify balance according to the amount of deposit


    withdraw : modify balance according to the amount of wothdrawal



2. ATM


    insert_card : request the card
  
  
    insert_pin : request the pin number

  
    choose_account : choose account from the connected accounts
  
  
    choose_action : choose transaction (see balance, deposit, withdraw, exit)
  
  
    see_balance : see the balance of the chosen account
  
  
    deposit : deposit to the chosen account
  
  
    withdraw : withdraw from the chosen account


3. AutoInput


    class just used to automatize the input for testing the codes


------
## How to run program


1. download the zip file
2. unzip it and move directory into it
3. run main.py



    p.s. You can manually enter inputs by uncommenting code at the bottom of the main.py



### Data set

                      card   pin         account  balance
    0  0000 0000 0000 0000  1234  110-110-111111       35
    1  1111 1111 1111 1111  3945  110-112-333333      745
    2  1111 1111 1111 1111  3945  110-283-282839      122
    3  2222 2222 2222 2222  1254  110-333-444444      923
    4  3333 3333 3333 3333  8989  110-283-283826     1283
    5  3333 3333 3333 3333  8989  210-382-383619       19
    6  3333 3333 3333 3333  8989  220-333-222222      363
  
