from abc import ABC , abstractmethod
class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    def withdraw(self):
        pass
class SavingAccount(Account):
    __balance = 0
    def get_balance(self):
        return self.get_balance
    
    def deposit(self,amount):
       # file = open("./type.txt","a")
        self.__balance += amount
        print("deposit amount" ,amount)
       # file.write(f"deposit:{amount}\n")
        #file.close()
        
    def withdraw(self,amount):
       # file = open("./type.txt","a")
        if self.__balance < amount:
            print("Not enough balance")
            return
        self.__balance -= amount
        print("Amount withdraw :",amount)
        #file.write(f"withdraw:{amount}\n")
        #file.close()
class CurrentAccount(Account): 
    __balance = 0
    withdrawlimit = 0
    
    def __init__(self,limit):
        self.withdrawlimit = limit
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        #file = open("./type.txt","a")
        self.__balance += amount
        print("deposite amount:",amount)
        #file.write(f"deposit:{amount}\n")
        #file.close() 
    def withdraw(self , amount):
        #file = open("./type.txt","a")
        if self.__balance < amount:
            print("Not enough")
            #file.write(f"withdraw:{amount}\n")
            #file.close()
            
        self.__balance -= amount
        print("withdraw account",amount)
class Bank:
    #file = open("./type.txt","a")
    owner = "SBI"
    acconut_number = 0
    account = None
    def __init__(self,name, number,account_type):
        
        self.owner = name
        self.account_number = number
        
        if account_type == "Savings":
            self.account = SavingAccount()
        if account_type == "Current":
            self.account = CurrentAccount(5000)
    #file.write(f"Account:{account}")
    #file.close()
            
class Manager:
    #file = open("./file.txt","a")
    def get_customer_info(self,bankAccount: Bank):
        print(f"Name : {bankAccount.owner}")
        print(f"AccountNumber : {bankAccount.account_number}")
        print("Account type :", end ="")
        
        if(type(bankAccount.account) == SavingAccount):
            print("saving Account")
        else:
            print("current Account")
            print(f"Balance : {bankAccount.account.get_balance()}")
    #file.write(f"bankaccount:{Bank}")
    #file.close()
    
    def __str__(self):
        return "Managerobject bro"
        
            
shiro = Bank("shiro", 1 ,"Savings")
shiro.account.deposit(500)
shiro.account.withdraw(150)
print(shiro.account.get_balance())

print("---- leo account-----")
leo= Bank("leo" , 2 , "Current")
leo.account.deposit(100)

vk = Manager()
print("----shiro Account-----")
vk.get_customer_info(shiro)
print("----leo account----")
vk.get_customer_info(leo)

           