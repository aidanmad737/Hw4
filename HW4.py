#setup variables
expense = 1
# Running list of every valid expense the user enters
expenses=[]
# Tallies for each category: small (< $25), moderate ($25-$100), large (> $100)
count_small = 0
count_large = 0
count_moderate = 0


#checking if expenses are not 0 and sorting them into categories
# Keep prompting until the user enters 0 to signal they are finished
while expense!= 0:
    print("Enter your Expenses:")
    expense = float(input())
    # Reject negative amounts and ask again
    if expense < 0:
        print("Please enter a valid expense amount.")
    elif expense != 0:
        expenses.append(expense)
        # Classify: under $25 is small, over $100 is large, everything else is moderate
        if expense < 25:
            count_small += 1
        elif expense > 100:
            count_large += 1
        else:
            count_moderate += 1
else:
    # Loop finished: print the summary statistics, formatted as dollars
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total: ${sum(expenses):,.2f}")
    print(f"Average: ${sum(expenses)/len(expenses):,.2f}")
    print(f"Minimum: ${min(expenses):,.2f}")
    print(f"Maximum: ${max(expenses):,.2f}")
    print(f"Number of small expenses: {count_small}")
    print(f"Number of moderate expenses: {count_moderate}")
    print(f"Number of large expenses: {count_large}")