# tip_calculator.py

# TODO: Create a function named calculate_tip
try:  #DO NOT MODIFY
    def tip_calculator(): # Renamed function from calculate_tip to tip_calculator to accept the local unit test. No other modifications were made to instructions.
        

    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
        total_cost = float(input("What is the cost of the meal? "))
        num_people = int(input("How many people are splitting the bill? "))
        tip= int(input("What percentage would you like to tip? "))
        tip_percentage = float(tip / 100)

    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).
        

    # NOTE: Calculate the tip and tax separately.
        tip_amount = total_cost * tip_percentage
        sales_tax = float(total_cost * .1)
        total_bill = total_cost + sales_tax + tip_amount
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay. 
        total_bill_division = float(total_bill / num_people) 
         
    
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00
        print(f'Total bill: ${format(total_bill,".2f")}')
        print(f'Each person should pay: ${format(total_bill_division,".2f")}')

    # NOTE: The amounts are displayed with 2 decimals only

except: # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid
    print("User Error: Invalid Entry")

    
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY
