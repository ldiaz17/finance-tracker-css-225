# Finance Tracker CSS-225 
# Author: Lea Diaz


# Step 1: Income
income = float(input("Enter your total income: "))

# Step 2: List to store categories and amounts
categories = []
amount = []

#Step 3: Input loop
while True:
  category = input("Enter expense category (or 'done' to finish): ")
  if category.lower() == "done":
    break 
  amount = float(input(f"Enter amount for {category}: "))
    categories.append(category)
    amounts.append(amount)

# Step 4: Calculate totals
total_expenses = sum(amounts)
remaining_balance = income - total_expenses

#Step 5: Print summary 
print("\n--- Finance Summary ---")
print("Total Income:", income)
print("Remaining Balance:", remaining_balance)
print("\nExpenses by Category:")

#Step 6: Print each category with the amount
for i in range(len(categories)):
  bar = '*' * int(amount[i] // 10)
print(categories[i], ":", amounts[i], "|", bar)                

    

