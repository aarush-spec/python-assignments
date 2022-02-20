class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner: Pavan \nAccount balance: 100"

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print("Deposit Accepted")

    def widthraw(self, wd_amt):
        try:
            if self.balance >= wd_amt:
                self.balance -= wd_amt
                print("Withdrwal accepted")
            else:
                print("Funds unavailable")
        except ValueError:
            print("valueerror for fund")

# Sir aur bhi kuch likhna tha kya muje samjha nhi.