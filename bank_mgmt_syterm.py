class Bank: 
    
    def __init__(self, name, bankname):
        self.name = name
        self.bankname = bankname
        
    def __str__(self): 
        return f"My name is {self.name} and my bank name is {self.bankname}."
    

c1 = Bank("Himanshu kumar", "Bank Of Baroda")
print(c1)
c2 = Bank("Shaumya kumari","Bank of Baroda")
print(c2)
c3 = Bank("Shubham Das", "Central Bank of India")
print(c3)