class BankAccount:
    bank_name="Metro Bank"
    next_account_id = 1000
    def __init__(self,account_holder, balance):
        self.id = BankAccount.next_account_id
        BankAccount.next_account_id += 1
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += int(amount)
        print(f"{amount} pounds depositted")
    def withdraw(self,amount):
         self.balance -= int(amount)
         print(f"{amount} pounds Withdrew")
    def display_info(self):
        print(f"Displaying info: \n {self.bank_name} | ID: {self.id} Balance: £{self.balance} | Holder: {self.account_holder}")
    
ali = BankAccount("Ali Jahankhah", 50000)
reza = BankAccount("Reza xyz",80000)
ali.display_info()
reza.display_info()
ali.bank_name = 'dfg'
ali.display_info()