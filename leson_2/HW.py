price = float(input('How mach it cost: '))
if price == 0:
    price = float(input('Price can`t be 0, please change price: '))
if price < 0:
    price = -price
    print('Price can`t be negative, change it to positive: ', price)
discount = float(input('Witch discount in % do you have?: '))
print('The discount is: ',discount, '%')
print('The prise is: ', price)
final_price = price
if discount == 0:
    print('discount is 0 ', discount)
if discount < 0:
    discount = -discount
    print('discount can`t be less 0 ', discount)
if discount > 0:
    final_price = price - ((price * discount)/100)
print( 'your final price: ', final_price)