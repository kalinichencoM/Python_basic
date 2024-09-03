# 1 Попросіть користувача ввести рядок і перевірте, чи є заданий рядок порожнім, конвертувавши його в булеве значення.

var_1 = input('Input text ')
var_1_bool = bool(var_1)

print('the text was added if True: ', var_1_bool)

# 2 Попросіть користувача ввести три числа, які в сумі дають 100, і перевірте це за допомогою assert. Якщо користувач ввів неправильно, виведіть йому помилку з написом на ваш розсуд.

print("Please insert 3 number with sum 100")
first_number = int(input('Input first number '))
second_number = int(input('Input second number '))
third_number = int(input('Input third number '))

suma = first_number + second_number + third_number

assert suma == 100, 'The sum is not 100'

print('Correct the sum is = ', suma)

# 3 Користувач повинен ввести пароль двічі для підтвердження. Необхідно перевірити, чи обидва введені паролі співпадають. Якщо паролі співпадають, вивести повідомлення 'пароль вірний' . Якщо паролі не співпадають, користувач отримує помилку.

print('Insert password 2 times: ')
first_time = input('Input password first time: ')
second_time = input('Input password second time: ')

assert first_time == second_time, "The password doesn't match"

print('The passwords is correct')