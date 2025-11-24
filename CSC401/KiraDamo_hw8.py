#written by Kira Damo

class TransitCard:
    'track transit card balance refills and rides charged'
    maxTransAmount = 100.00 #class variable
    maxCardBalance = 350.00 #class variable

    def __init__(self, amount=5.00):
        'initializes transit card with balance amt up to $100 or default amount of $5'
        self.a=amount #instance variable
        if amount >= TransitCard.maxTransAmount:
            raise ValueError ('Amount is greater than 100')
        return
           
    def __repr__(self):
        'canonical repressenataion of constructor'
        return 'Card balance is {:6.2f}'.format(self.a)

    def balance(self):
        'returns balance when called'
        return self.a

    def ride(self, fare):
        'decreases balance when user spends ride fare'
        if self.a <= 0:
            raise ValueError ('Card balance is 0 or negative; ride is denied')
            return
        elif self.a > 0 and self.a < fare:
            self.a = self.a - fare
        elif self.a > 0 and fare < self.a:
            self.a = self.a - fare
            
    def addValue(self, amount):
        'increases amount when user loads card up to 350'
        if amount > TransitCard.maxTransAmount:
            raise ValueError ('Amount is > 100.00')
            return
        elif self.a + amount > TransitCard.maxCardBalance:
            raise ValueError ('Card balance will be greater than 350.00. Request denied')
            return
        self.a += amount
   
