# coding: utf-8
import math
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
# Creating a list will all loan costs.
loan_costs = [500, 600, 200, 1000, 450]


# Test on if i remembered how to call with len 
# len(loan_costs)
# print(len(loan_costs))


# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

print("PART 1")
print("----------------------")
print(

    
)
# Directly pulling the number of loans via the len fuction and printing it 
len(loan_costs)
print(f"The total number of loans is: {len(loan_costs)}")
print(

    
)
# Storing the number of loans in a variable
ttl_loans = len(loan_costs)

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

# Summing up all indexes in the list via the sum function and printing it
sum(loan_costs)
print(f"The sum of all loans in the list is: {sum(loan_costs)}")
print(

    
)
# Storing the sum of all indexes in loan_costs list in a variable.
sum_loans = sum(loan_costs)

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

# Creating the average loan amount with math utilzing created variables and printing it.
avg_loan_amt = sum_loans/ttl_loans
print(f"The average loan amount is: {avg_loan_amt}")
print(

    
)

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
# Creates a dictionary
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

# Retrieves the future value from the dictionary using the get cmd and assigning it to a variable
ftr_val = loan.get("future_value")
#  Retrieves the remaining months from the dictionary using the get cmd and assigning it to a variable
rmn_mth = loan.get("remaining_months")
print("PART 2")
print("----------------------")
print(


)
# Prints the value stored in the previosly created future value variable
print(f"The future value of the loan is: {ftr_val}")
print(

    
)
# Prints the value stored in the previosly created remaining months variable
print(f"The remaining number of months on the loan is: {rmn_mth}")
print(

    
)

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# YOUR CODE HERE!

# Using Math 
# denom = math.pow((1+(.2/12)), rmn_mth)
# present_value = ftr_val / denom 

# Creating the discount rate variable and setting it equal to .2 = 20%
disc_rate = .2
# Calculates the present value of the loan using math with parameters of previously created variables and storing it in a present value variable.
present_value = (ftr_val) / ((1+(disc_rate/12)) ** rmn_mth)
# Prints the stored value of present value and rounds it to two decimal places.
print(f"The Present Value of the loan is: ${round(present_value, 2)}")
print(

    
)

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

# This checks if the present value of the loan is greater than or equal to the cost of the loan found in the previously referenced loan dictionary.
if present_value >= loan.get("loan_price"):
    # If this check passes then it prints the statement below.
    print("The loan is worth at least the cost to buy it.")
# If the above condition fails, the below condition is executed.
else:
    # Printing the failure case
    print("The loan is too expensive and not worth the price.")
print(

    
)

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
# Creates a new loan dictionary 
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

print("PART 3")
print("----------------------")
print(


)
# Creates a different future value variable that is pulled from the new dictionary via the get function. 
futr_val = new_loan.get("future_value")
# Creates a different remaining months variable that is pulled from the new dictionary via the get function.
remn_mth = new_loan.get("remaining_months")
# Creating a function that can return the present value of the new loan using parameters future value, remaining months, and the annual discount rate.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    # Creating a present value variable within the function using the above present value formula and newly generated variables as parameters.
    present_value = futr_val / ((1+(annual_discount_rate/12)) ** remn_mth)
    # Returns the calulated value into the present value variable and displays it
    return present_value




# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

# Creating a new discount rate variable
annual_discount_rate = .2

# Unecessary code I believe 
# ftr_val = new_loan.get("future_value")
# rmn_mth = new_loan.get("remaining_months")

# Using the calculate present value formula using new parameters 
calculate_present_value(futr_val, remn_mth, annual_discount_rate)
# Stores the present value in a variable called result
result = calculate_present_value(futr_val, remn_mth, annual_discount_rate)

# Prints the newly found Present Value and rounds it to the second decimal place.
print(f"The Present Value of the new loan is: ${round(result, 2)}.")
print(

    
)

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
print("PART 4")
print("----------------------")
print(


)
# Creates a list comprised of dictionaries 
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

# Creates an empty list titled inexpensive loans 
inexpensive_loans = []


# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

# loops the the loans list for every i, i being each individual dictionary
for i in loans:
    # Conditional where it checks if the loan price found in dictionary "i" is less than or equal to 50 
    if i["loan_price"] <= 500:
        # If the above passes, the below will apend dictionary "i" into the previosuly empty inexpensive loans list
        inexpensive_loans.append(i)

   
# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!
# prints the inexpensive loans list
print(inexpensive_loans)

# """Part 5: Save the results.

# Output this list of inexpensive loans to a csv file
#     1. Use `with open` to open a new CSV file.
#         a. Create a `csvwriter` using the `csv` library.
#         b. Use the new csvwriter to write the header variable as the first row.
#         c. Use a for loop to iterate through each loan in `inexpensive_loans`.
#             i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

#     Hint: Refer to the official documentation for the csv library.
#     https://docs.python.org/3/library/csv.html#writer-objects

# """

# # Set the output header
# This will make the top of the excel sheet be organized by the below names 
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# # Set the output file path
# Creates a path where it will name and save the csv file
output_path = Path("inexpensive_loans.csv")
# Something to explain what is going on
print("Saving to .csv file...")

# # @TODO: Use the csv library and `csv.writer` to write the header row
# # and each row of `loan.values()` from the `inexpensive_loans` list.
# # YOUR CODE HERE!



# open the above newly created path and overwrites data
# opens the csv file for writing
with open(output_path, 'w', newline= '') as csvpath:
    # creates a csv writer using the writer function
    csv_writer = csv.writer(csvpath)
    # writes data into the csv file by using the writerow function of the writer
    csv_writer.writerow(header)
    # loops the above through the inexpensive loans lists and writes it into the csv
    for loans in inexpensive_loans:
        csv_writer.writerow(loans.values())






# This was just testing and practice 
# lp1 = loans[0]['future_value']
# lp2 = loans[1]['future_value']
# lp3 = loans[2]['future_value']
# lp4 = loans[3]['future_value']

# for x in range(len(loans)):
#     print(x) 
# will print out indexes of dicts

# for x in range(len(loans)):
    # range of 0-3 
    # print(loans[x])
# prints actual dictionaries 

# print(loans[0])