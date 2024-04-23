class Customer:
    def __init__(self, first_name, last_name, id_number, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.phone = phone
    
    def display_info(self):
        print("Customer Information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("ID Number:", self.id_number)
        print("Phone Number:", self.phone)


class Account(Customer):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer.first_name, customer.last_name, customer.id_number, customer.phone)
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited {} TL.".format(amount))
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn {} TL.".format(amount))
        else:
            print("Insufficient balance!")
    
    def display_balance(self):
        print("Account Balance:", self.balance)


# Creating a customer
customer = Customer("Ahmet", "Yılmaz", "12345678901", "5555555555")

# Creating an account and adding customer information
account = Account(customer, "123456789", 1000)

# Account operations
account.display_info()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Shouldn't be possible due to insufficient balance
account.display_balance()