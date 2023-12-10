class RentalProperty():

    def __init__(self):
        return self
    
    def totalMonthlyIncome(self):
        self.rent_amount = int(input("How much is the rent?: "))
        self.laundry_amount = int(input("How much is the laundry?: "))
        self.storage_amount = int(input("How much is storage?: "))
        self.misc_amount =  int(input("Total miscellaneous charges for your tenant?: "))

        self.total = self.rent_amount + self.laundry_amount + self.storage_amount + self.misc_amount
        return self.total
    
    def monthlyExpences(self):
        
