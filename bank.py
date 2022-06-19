
from datetime import datetime


class Account:
    def __init__(self,name,phone_number,account_number,id):
        self.name=name
        self.phone_number=phone_number
        self.account_number=account_number
        self.id=id
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=100
        self.loan_balance=0
        
    
    def withdraw (self,amount):
        self.amount=amount
        date=datetime.now()
       
        if amount>self.balance:
            return f"Dear customer, you have insuffient funds for this withdraw"
        elif amount<=0:
            return f"Dear customer, you can't withdraw zero amount "            
        else:
             self.balance -=amount
             dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for withdrawing {amount} on {date}'}
             self.withdrawals.append(dct)
        withdrawal_amount=self.balance-self.transaction
        if amount>withdrawal_amount:
            return "insufficient balance"
        self.balance-=amount+self.transaction
        return f"You have withdrawn Ugshs.{self.withdrawals} and your new balance is {self.balance} on {date.strftime('%d/%m/%Y')})"
              
      
    def deposit(self,amount):
        date=datetime.now()
        self.amount=amount
        if amount<=0:
            return f"deposit amount must be greater than zero(0)"
        else:
             self.balance+=amount
             dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for depositing {amount} on {date}'}
             self.deposits.append(dct)
             
             return f"Hello you have deposited{amount} and your new balance is {self.balance})"
    
         
    def deposit_statement(self):
        for x in self.deposits:
            print (x)
    def withdraw_statement(self):
        for y in self.withdrawals: 
            print(y)
         
    def current_balance(self):
        return f" Your current balance is  {self.balance}" 
    
    def full_statement(self):
        statement=self.deposits+self.withdrawals
        for a in statement:
            print(a["narration"])    
    def borrow(self,amount):
        sum=0
        for y in self.deposits:
            sum+=y["amount"]
            
        if len(self.deposits) <10:
            return f"you are not eligible to borrow.make {10-len(self.deposits)} to borrow "
        if amount<100:
            return f"you can borrow atleast 100"  
        if amount>sum/3:
            return f"you can borrow upto {sum/3}" 
        if self.balance!=0:
            return f"you have {self.balance} you can not borrow yet you still have balance on your account"
        if self.loan_balance!=0:
            return f"you have a debt of {self.loan_balance} you have to pay first for you to borrow."
        else:
            interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            return f"you have borrowed {amount} your loan is now at {self.loan_balance}"
    
    def loan_repayment(self,amount):
        
         if amount>self.loan_balance:
             self.balance+=amount-self.loan_balance
             self.loan_balance=0
             return f" thank you for paying the loan of {amount-self.loan_balance} your account balance is {self.balance}"
               
         else:
             self.loan_balance-=amount
             return f"thank you"
            
         
    def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return f"insuficient funds"
        if isinstance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f" Hello you have sent {amount} to {new_account} with the name {new_account.name}.your new balance is {self.balance}"