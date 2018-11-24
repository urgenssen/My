
def format_price(price):
	new_price = int(price)
	return "Цена: " + str(new_price) + " руб."

display_price = format_price(56.24)
print(display_price)
