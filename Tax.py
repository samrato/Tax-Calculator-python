def main():
    # User input
    name = input("Hello, our dear customer. Enter your full name: ")
    gender = input("What is your gender? ")
    income = int(input("Please enter your total income: "))
    number_of_children = int(input("How many children do you have? "))

    # Validate inputs
    if income < 0 or number_of_children < 0:
        print("Invalid inputs")
        return

    # Calculate credit
    if income >= 110000:
        credit = 0
    elif number_of_children <= 3:
        credit = number_of_children * 1000
    else:
        credit = 3000

    # Calculate income tax based on income brackets
    if income <= 1850:
        income_tax = income * (10 / 100)
    elif income <= 73800:
        income_tax = 1815 + ((income - 1850) * (15 / 100))
    elif income <= 148850:
        income_tax = 10162.5 + ((income - 73800) * (25 / 100))
    elif income <= 225850:
        income_tax = 28925 + ((income - 148850) * (28 / 100))
    elif income <= 405100:
        income_tax = 50765 + ((income - 225850) * (33 / 100))
    elif income <= 457600:
        income_tax = 109587.5 + ((income - 405100) * (35 / 100))
    else:
        income_tax = 127962.5 + ((income - 457600) * (39.6 / 100))

    # Calculate total tax after applying credit
    total_income_tax = max(0, income_tax - credit)

    # Convert to other currencies
    income_in_pounds = total_income_tax * 20
    income_tax_in_euros = total_income_tax / 155.92
    income_tax_in_dollars = total_income_tax / 147.07

    # Output results
    print(f"The credit for you is: {credit}")
    print(f"The income tax for you is: {income_tax}")
    print(f"The total income tax to be charged is: {total_income_tax}")
    print(f"HELLO {name.upper()}, WELCOME BACK AGAIN TO OUR COMPANY. WE VALUE YOUR INTEREST")
    print("\nTHE EXCHANGE RATES OF YOUR INCOME TAX ARE AS FOLLOWS.....\n")
    print(f"Your income tax in pounds is: {income_in_pounds:.2f} pounds")
    print(f"Your income tax in euros is: {income_tax_in_euros:.2f} euros")
    print(f"Your income tax in dollars is: {income_tax_in_dollars:.2f} dollars")

if __name__ == "__main__":
    main()
