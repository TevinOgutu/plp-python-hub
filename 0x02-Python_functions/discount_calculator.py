def calculate_discount(price, discount_percent):
   if discount_percent >= 20:
       final_price = price * (1 - discount_percent / 100)
       return final_price
   else:
       return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price == original_price:
   print(f"No discount applied. The final price is: {final_price}")
else:
   print(f"The final price after applying the {discount_percent}% discount is: {final_price}")
