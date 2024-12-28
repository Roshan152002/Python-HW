class Atm:
    def __init__(self):
        self.__pin = '' 
        self.__balance = 0
        
        self.__menu()

    def __menu(self):
        choice = input("""
                Hello , how would you like to proceed ?
                1. Create Pin.
                2. Deposit Money.
                3. Withdraw Money.
                4. Check Balance.
                5. Exit
        """)
    
        self.check_choice(choice)
    
    def get_pin(self):
        return self.__pin
    
    
    def check_choice(self,choice):
        match choice:
            case '1':
                self.create_pin()
            case '2':
                self.deposit()
            case '3':
                self.withdraw()
            case '4':
                self.check_balance()
            case '5':
                print("Exiting...")
                exit()

    def create_pin(self):
        self.__pin = input("Enter Pin:")
        print('Pin created successfully !')
        self.menu()


    def deposit(self):
        temp_pin = input('Enter your pin to deposit money :')
        if temp_pin == self.__pin:
           amount = int(input('Enter the amount :')) 
           self.__balance = self.__balance + amount
           print('Amount Added Successfully !')
        else:
            print('Invalid Pin Entered !')

        self.menu()
        

    def withdraw(self):
        temp_pin = input('Enter your pin to withdraw the money :')
        if temp_pin == self.__pin:
            amount = int(input('Enter amount to be withdrawl:'))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Take your cash ...")
                print('Withdrawl operation successfully done !')
            else:
                print('Insuficient balance !!')
        else:
            print('Invalid Pin !')
        
        self.menu()
        
    
    def check_balance(self):
        print(f'Your available balance is {self.__balance}')

        self.menu()



# if you declare your instance variable to private variable then it converts __var to obj.Atm__var 
# obj.Atm__var you can access this outside of class . then what's use of private variable
# python is not purely private var/obj

sbi = Atm()

print(sbi.get_pin())