class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars = dollars  
        self.cents = cents    


# getter setter





    def get_dollars(self):
        return self.dollars   
    # result=0

    def get_cents(self):
        return self.cents
    # result=0
    

    def set_dollars(self, dollars):
        self.dollars = dollars

    def set_cents(self, cents):
        self.cents = cents

    

    def add_dollars(self, amount):
        self.dollars += amount

    def add_cents(self, amount):
        total_cents = self.dollars * 100 + self.cents + amount
        self.dollars = total_cents // 100
        self.cents = total_cents % 100

    # only for depositing 
    def __add__(self, other):
        total_cents = self.dollars * 100 + self.cents + other.dollars * 100 + other.cents
        result_dollars = total_cents // 100
        result_cents = total_cents % 100
        return Money(result_dollars, result_cents)
    
    # only for withdrawing 
    def __sub__(self, other):
        total_cents = self.dollars * 100 + self.cents - (other.dollars * 100 + other.cents)
        if total_cents < 0:
            raise ValueError("Not enough funds in the account.")
        result_dollars = total_cents // 100
        result_cents = total_cents % 100
        return Money(result_dollars, result_cents)

    def __mul__(self, other):
        total_cents = self.dollars * 100 + self.cents
        result_cents = total_cents * other
        result_dollars = result_cents // 100
        result_cents = result_cents % 100
        return Money(result_dollars, result_cents)

    def __str__(self):
        return f"${self.dollars}.{self.cents:02d}"

    def __eq__(self, other):
        return self.dollars == other.dollars and self.cents == other.cents

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, index):
        if index == 0:
            return self.dollars
        elif index == 1:
            return self.cents
        else:
            raise IndexError("Invalid index. Index must be 0 for dollars or 1 for cents.")
        

