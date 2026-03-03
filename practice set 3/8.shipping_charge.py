amount = int(input('Enter Amount of the Order -> ₹'))
ship_dis = 0
ship = 0

if amount < 1500:
    ship = 100
    ship_dis = 80
elif amount > 1500 and amount <= 3000:
    ship = 70
    ship_dis = 50
elif amount > 3000:
    ship = 0

print("\n===============================================================")
print("\t\t   🛒 FINAL BILL SUMMARY")
print("===============================================================")
print(f"Shopping Amount: \t\t\t ₹ {amount}")

if ship == 0:
    print("Shipping:\t\t\t\t FREE 🚚")
    dis = (amount * 7) / 100
    print(f"Discount (7%):\t\t\t\t -₹ {dis:.2f}")
    print("\t\t\t\t---------------------")
    print(f"💰 Total Payable Amount:\t\t ₹ {amount - dis:.2f}")
    print("\t\t\t\t---------------------")
    print("✅ Congratulations! You got Free Shipping and 7% Discount!")
else:
    next_offer = abs(amount - 1500)
    print(f"\n⚠️  Add ₹{next_offer} more to get FREE SHIPPING worth ₹{ship_dis}!")
    print(f"Shipping Charge:\t\t\t +₹ {ship}")
    print("\t\t\t\t---------------------")
    print(f"💰 Total Payable Amount:\t\t ₹ {amount + ship:.2f}")
    print("\t\t\t\t---------------------")
    print("🛍️  Thank you for shopping with us! 😊")

print("===============================================================\n")
