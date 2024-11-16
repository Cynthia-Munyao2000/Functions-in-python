# Function to calculate the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply discount
        discount = (discount_percent / 100) * price
        final_price = price - discount
        return final_price
    else:
        # No discount applied
        return price

# Prompting user for input
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the result
final_price = calculate_discount(price, discount_percent)

# Print the result based on the discount applied
if final_price == price:
    print(f"No discount applied. The original price is: ${price:.2f}")
else:
    print(f"The final price after applying the {discount_percent}% discount is: ${final_price:.2f}")
