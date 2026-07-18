#Step 1: Define the class
class Loan1 :
        #Step 1.1: Initialize the loan with the specified values
        def __init__(self, annual_interest_rate, number_of_years, loan_amount) :
                self.__annual_interest_rate = annual_interest_rate
                self.__number_of_years = number_of_years
                self.__loan_amount = loan_amount
        #Step 1.2: Define the method that calculates the amount of monthly payments on the loan
        def get_monthly_payment(self) :
                monthly_interest_rate = self.__annual_interest_rate / 12
                monthly_payment = self.__loan_amount * monthly_interest_rate / (1 -
                                (1 / (1 + monthly_interest_rate) ** (self.__number_of_years * 12) ))
                return monthly_payment
        #Step 1.3: Define the methods to get/set the properties of the loan
        def get_annual_interest_rate(self) :
                return self.__annual_interest_rate
        def set_annual_interest_rate(self, annual_interest_rate) :
                self.__annual_interest_rate = annual_interest_rate
        def get_number_of_years(self) :
                return self.__number_of_years
        def set_number_of_years(self, number_of_years) :
                self.__number_of_years = number_of_years
        def get_loan_amount(self) :
                return self.__loan_amount
        def set_loan_amount(self, loan_amount) :
                self.__loan_amount = loan_amount
#Step 2: Test the class
annual_interest_rate = float(input("Enter the annual interest rate: "))
number_of_years = int(input("Enter the number of years for the loan period: "))
loan_amount = (float(input("Enter the loan amount: ")))
loan1 = Loan1(annual_interest_rate, number_of_years, loan_amount)
print("The monthly payment for the loan is: {:.2f} ".format(loan1.get_monthly_payment()))
