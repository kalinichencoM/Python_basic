var_1 = 10
new_var = bool(var_1)
print(type(new_var), new_var)
print()

var_true = True
var_false = False
print(type(var_true), var_true)
print(type(var_false), var_false)
print()

print(True and False) # False
print(True and True) # True

print(False or True) # True
print(False or False) # False
print(True or True) # True

print(not False) # True
print(not True) # False

first_number = 10
second_number = 10
third_number = 5

print(id(first_number))
print(id(second_number))
print(id(third_number))

print(first_number is second_number) #True
print(first_number is third_number) #False

print(first_number==second_number) # True
print(second_number==third_number) # False

print(first_number!=second_number) # False
print(second_number!=third_number) # True

answer_1 = int(input('2 + 3 ='))
assert answer_1 == 5, "Wrong the answered 5."

print('correct answer')
print('next question')

answer_2 =  int(input('7 + 3 ='))
assert answer_2 == 10,  "Wrong the answered 10."
print('Well done!')