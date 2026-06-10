cartValue = int(input("Enter cart value: "))
isPrimeMember = input("Are you a Prime Member? (yes/no): ").lower() == "yes"
isFestivalDay = input("Is today Festival Day? (yes/no): ").lower() == "yes"
paymentMode = input("Enter payment mode (Credit/Debit/UPI): ").lower()


discount = 0
if cartValue >= 5000 and isPrimeMember:
    discount = 20
elif cartValue >= 5000 and not isPrimeMember:
    discount = 10


# Step 2: Extra discount if Festival Day
if isFestivalDay:
    discount += 5  #discount=discount+5

# Apply discount
finalPrice = cartValue - (cartValue * discount / 100)

# Step 3: Cashback if payment mode is Credit Card
cashback = 0
if paymentMode == "credit":
    cashback = 200


# Step 4: Final check (cannot go below 3000)
if finalPrice < 3000:
    finalPrice = 3000