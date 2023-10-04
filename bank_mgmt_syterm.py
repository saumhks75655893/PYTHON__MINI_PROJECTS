class Bank: 
    
    def __init__(self, name, bankname):
        self.name = name
        self.bankname = bankname
        
    def __str__(self): 
        return f"My name is {self.name} and my bank name is {self.bankname}."
    

c1 = Bank("Himanshu kumar", "Bank Of Baroda")
print(c1)