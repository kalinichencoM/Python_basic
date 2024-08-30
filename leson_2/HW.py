price = float(input('How mach it cost: '))
discount = float(input('Witch discount in % do you have?: '))
print('The discount is: ',discount, '%')
print('The prise is: ', price)
if discount == 0:
    print('discount is 0 ', discount)
    print('your final price: ', price)
if discount < 0:
    print('discount can`t be less 0 ', discount)
    print('your final price: ', price)
if discount > 0:
    final_price = price - ((price * discount)/100)
    print( 'your final price: ', final_price)