class Bank: 
    
    def __init__(self, name, Bank_Name, DOB): 
        self.name = name
        self.Bank_name = Bank_Name
        self.DOB = DOB
        
    
B1 = Bank("himanshu ", "Bank of Baroda", "10/06/2003")

print(B1.name)
print(B1.Bank_name)
print(B1.DOB)