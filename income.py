class ROICalculator():

    def __init__(self):
        return self
    
    def totalMonthlyIncome(self):
        """
            totalMonthlyIncome() expects the amount for rent, laundry, storage, and miscellaneous items
            and returns the total estimated amount for the month.
        """
        self.rent_amount = int(input("How much is the rent?: "))
        self.laundry_amount = int(input("How much is the laundry?: "))
        self.storage_amount = int(input("How much is storage?: "))
        self.misc_amount =  int(input("Total miscellaneous charges for your tenant?: "))

        self.totalIncome = self.rent_amount + self.laundry_amount + \
            self.storage_amount + self.misc_amount
        return self.totalIncome
    
    def monthlyExpences(self):
        """
            monthlyExpenses() expects the amount for taxes and several other applicable amounts paid by the owner
            and returns the total of that for the month

        """
        self.taxes = int(input("What are the taxes on the property?: "))
        self.insurance = int(input("What are the monthly insurance payments?: "))
        self.water = int(input("Water cost?: "))
        self.waste = int(input("Waste cost?: "))
        self.electric = int(input("Electric cost?: "))
        self.hoa = int(input("HOA fee?: "))
        self.landscaping = int(input("Landscaping cost?: "))
        self.vacancy = int(input("Vacancy cost?: "))
        self.repairs = int(input("Repairs cost?: "))
        self.capEx = int(input("Cap Ex?: "))
        self.propertyManagement = int(input("Property Management figure?: "))
        self.mortgage = int(input("Mortgage amount?: "))

        self.utilities = self.water + self.electric + self.waste

        self.totalExpense = self.taxes + self.insurance + \
            self.utilities + self.hoa + self.landscaping + \
            self.vacancy + self.repairs + self.capEx + \
            self.propertyManagement+self.mortgage

        return self.totalExpense
    
    def cashFlowMonthly(self):
        """
            cashFlow() Calculates the totalExpense from totalIncome
        """

        self.monthlyCashflow = self.totalIncome - self.totalExpense
        return self.monthlyCashflow




