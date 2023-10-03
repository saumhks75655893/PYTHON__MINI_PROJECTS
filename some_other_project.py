class master: 
    
    def __init__(self, name, rollNO):
        self.name = name
        self.rollNO = rollNO
     
    def __str__(self):
        return f"My name is {self.name} and my roll number is {self.rollNO}. "
    
m1 = master("himanshu", 20)
print(m1)