square_meters = int(input("How many squarem. is going to be prepared? "))
full_yard = square_meters * 7.61
discount = 0.18 * full_yard
final_price = full_yard - discount

print(f"The final price is {final_price} and the discount is {discount}")
