#take inputs for cost price and discount
cost_price=float(input('Enter Cost Price of a Book:'))
discount_percent=float(input('Enter Discount:'))

#calculate discount amount
discount_amount = (discount_percent/100) * cost_price
selling_price = cost_price - discount_amount

#display result
print(selling_price)
print(f'Selling Price of a Book is {selling_price}rs.')

