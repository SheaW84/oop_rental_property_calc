class ROICalculator():

    def __init__(self, total_income, total_expense, annual_cash_flow, cash_return):
         self.total_income = total_income
         self.total_expense = total_expense
         self.annual_cash_flow = annual_cash_flow
         self.cash_return = cash_return
    
    def totalMonthlyIncome(self):
        """
            totalMonthlyIncome() expects the amount for rent, laundry, storage, and miscellaneous items
            and returns the total estimated amount for the month.
        """
        rent_amount = int(input("How much is the rent?: "))
        laundry_amount = int(input("How much is the laundry?: "))
        storage_amount = int(input("How much is storage?: "))
        misc_amount =  int(input("Total miscellaneous charges for your tenant?: "))

        self.total_income = rent_amount + laundry_amount + \
            storage_amount + misc_amount
        
        return self.total_income
    
    def monthlyExpences(self):
        """
            monthlyExpenses() expects the amount for taxes and several other applicable amounts paid by the owner
            and returns the total of that for the month

        """
        taxes = int(input("What are the taxes on the property?: "))
        insurance = int(input("What are the monthly insurance payments?: "))
        water = int(input("Water cost?: "))
        waste = int(input("Waste cost?: "))
        electric = int(input("Electric cost?: "))
        hoa = int(input("HOA fee?: "))
        landscaping = int(input("Landscaping cost?: "))
        vacancy = int(input("Vacancy cost?: "))
        repairs = int(input("Repairs cost?: "))
        capEx = int(input("Cap Ex?: "))
        propertyManagement = int(input("Property Management figure?: "))
        mortgage = int(input("Mortgage amount?: "))

        utilities = water + electric + waste

        self.total_expense = taxes + insurance + \
            utilities + hoa + landscaping + \
            vacancy + repairs + capEx + \
            propertyManagement + mortgage
        
        return self.total_expense
    
    def cashFlowMonthly(self):
        """
            cashFlow() Calculates the totalExpense from totalIncome
        """
        monthly_cash_flow = self.total_income - self.total_expense
        self.annual_cash_flow = monthly_cash_flow * 12

        return self.annual_cash_flow
    
    def cashOnCash(self):
        """
            cashOnCash() expects the downpayment, closing cost, rehab budget, and other miscellaneous expenses
            and sums it to the total_investment. 

        """
        downpayment = int(input("Planned downpayment?: "))
        closing_cost = int(input("Discussed closing cost?: "))
        rehab_budget = int(input("Rehab budget?: "))
        misc_expenses = int(input("Other expenses?:"))

        total_investment = downpayment + closing_cost +\
            rehab_budget + misc_expenses
        
        self.cash_return = self.annual_cash_flow / total_investment * 100
        
        print(f"Cash on cash return %{float(self.cash_return,2)}")

    def run(self):


        print("This is the Return On Investment Calculator")
        new_ROI.totalMonthlyIncome()
        new_ROI.monthlyExpences()
        new_ROI.cashFlowMonthly()
        new_ROI.cashOnCash()





new_ROI = ROICalculator(1,1,1,1)
new_ROI.run()


        





